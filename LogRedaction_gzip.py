import os
import datetime
import gzip
import shutil

# These Global variables can be modified
directory_input = 'InputFiles'
directory_output = 'OutputFiles'
match_string = [b" CC=", b" SSN="]  # must be list of bytes
archive_input = 'no'  # 'yes' allows the archive of input files. 'no' will prevent archive of input files


def archive_file_redaction(dir_in, dir_out, dt, ai):
    # Creates new datetime named archive folder and archives files into them.
    # Does this for output files every time and input files if the archive_input is set to 'yes'
    dir_in_arch = os.path.join(dir_in, str(dt))
    dir_out_arch = os.path.join(dir_out, str(dt))

    # ++ Input Archive ++ #
    if ai == 'yes':  # checks if we are archiving input files or not
        os.mkdir(dir_in_arch)  # Create archive folder within dir_in including datetime(dt)
        for filename in os.scandir(dir_in):
            # Move all files under input directory into new archive folder
            filepath_arch_in = os.path.join(dir_in_arch, filename.name)
            if os.path.isdir(filename):
                continue
            else:
                shutil.move(filename, filepath_arch_in)

    # ++ Output Archive ++ #
    os.mkdir(dir_out_arch)  # Create archive folder within dir_out including datetime(dt)
    for filename in os.scandir(dir_out):
        # Move all files under output directory into new archive folder
        filepath_arch_out = os.path.join(dir_out_arch, filename.name)
        if os.path.isdir(filename):
            continue
        else:
            shutil.move(filename, filepath_arch_out)


def single_file_redaction(dir_in, fn, dir_out, match_str):
    # This function processes one file for file redaction
    # -- inputs --
    # dir_in - Directory for Input Files
    # fn - filename
    # dir_out - directory for output of Files
    # match_string - list of strings to match to lines to flag for redaction (inclusive OR)
    line_count = 0  # will count total number of lines in file
    line_count_faulty = 0  # will count total number of faulty lines that match the string for redaction
    fn_output = fn[0:-3]  # filename sans '.gz'. This will need to change if filetype changes.
    fn_output_compressed = str(fn_output) + '.gz'  # adds the .gz back for compressed file
    with gzip.open(os.path.join(str(dir_in), str(fn)), 'rb') as file:
        while True:
            line = file.readline()
            # Open the output (redacted) file to append only good lines to. Creates file if it does not exist already
            # Initial file will be compresed as .gz after lines are copied
            with open(os.path.join(str(dir_out), str(fn_output)), 'ab') as file_output:
                if any(x in line for x in match_str):
                    # Checks if current line in file contains any of the strings in the match_string.
                    line_count_faulty += 1
                    # Notice that we do not write this line to the new file because it is faulty
                else:
                    file_output.write(line)
                    # Writes to output file if no match. Essentially leaving out the 'faulty' lines in the new file
            if not line:
                # End of the file
                with open(os.path.join(str(dir_out), str(fn_output)), 'rb') as file_output:
                    # Compress the file into new .gz file
                    with gzip.open(os.path.join(str(dir_out), str(fn_output_compressed)), 'ab') \
                            as file_output_compressed:
                        shutil.copyfileobj(file_output, file_output_compressed)
                    # End Compress of file
                os.remove(os.path.join(str(dir_out), str(fn_output)))
                # delete the text file now that we have a compressed file
                print('Final Lines: ' + str(line_count) + ' processed.')
                print('Final Faulty Lines: ' + str(line_count_faulty) + ' processed.')
                return [line_count, line_count_faulty]
                # returns list [0]total lines in file and [1]faulty lines. main() uses this to write to audit log
            line_count += 1
            # uncomment below line to see output of each line being processed
            # print('Line: ' + str(line_count) + ' processed.')


def main():
    date_time_now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    audit_log_name = 'LogRedactionAuditLog_' + str(date_time_now) + '.txt'

    with open(os.path.join(str(audit_log_name)), 'a') as file_audit_log:
        file_audit_log.write('+++++++ LOG REDACTION AUDIT LOG - ' + str(date_time_now) + '. +++++++\n')
    # Create Audit Log File
    for filename in os.scandir(directory_input):
        # Process each object under the directory
        print('Processing ' + filename.name + '...')
        if os.path.isdir(filename):
            # If the object is a directory, ignore
            continue
        else:
            if '.gz' in filename.name:
                # File is a .gz file, so run the single file redaction function on it and log the results
                count_list = single_file_redaction(directory_input, filename.name, directory_output, match_string)
                with open(os.path.join(str(audit_log_name)), 'a') as file_audit_log:
                    file_audit_log.write('File Processed: ' + str(filename.name) + ', ' + 'Total Lines ' +
                                         str(count_list[0]) + ', ' + 'Total Faulty Lines: ' + str(count_list[1]) + '\n')
                # End of .gz file processing
            else:
                # File is not a .gzip so throw a warning and exit
                print('WARNING: ' + filename.name + ' not a .gz file. It will not be processed')
                with open(os.path.join(str(audit_log_name)), 'a') as file_audit_log:
                    file_audit_log.write('File not a .gz file: ' + str(filename.name) + ': not processing' + '\n')
    archive_file_redaction(directory_input, directory_output, date_time_now, archive_input)
    # Archive the output files, and also the input files if the flag is set


if __name__ == "__main__":
    main()
