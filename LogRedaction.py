import os
import datetime

"""
Comments added here between three "s
https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/
"""


def single_file_redaction(dir_sf, fn, dir_out, aln):
    line_count = 0
    line_count_faulty = 0
    match_string = ["CC=", "SSN="]
    fn_output = str(fn) + '_output.txt'
    with open(os.path.join(str(dir_sf), str(fn)), 'r') as file:
        print('creating output file...')
        while True:
            line = file.readline()
            # Open the output (redacted) file to append only good lines to
            with open(os.path.join(str(dir_out), str(fn_output)), 'a') as file_output:
                # Checks if line in file contains anything in the match_string. Writes to output file if not.
                if any(x in line for x in match_string):
                    line_count_faulty += 1
                else:
                    file_output.write(line)
            if not line:
                # Logic here to write to audit log
                with open(os.path.join(str(aln)), 'a') as file_audit_log:
                    file_audit_log.write('File Processed: ' + str(fn) + ', ' + 'Total Lines ' + str(line_count) +
                                         ', ' + 'Total Faulty Lines: ' + str(line_count_faulty) + '\n')
                print('Total Lines: ' + str(line_count))
                print('Total Faulty Lines: ' + str(line_count_faulty))
                return [line_count, line_count_faulty]
            line_count += 1
            print('Line: ' + str(line_count) + ' processed.')



def main():
    directory = 'SampleFiles'
    directory_output = 'OutputFiles'
    date_time_now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    audit_log_name = 'LogRedactionAuditLog.' + str(date_time_now) + '.txt'
    with open(os.path.join(str(audit_log_name)), 'a') as file_audit_log:
        file_audit_log.write('+++++++ LOG REDACTION AUDIT LOG - ' + str(date_time_now) + '. +++++++\n')
    for filename in os.scandir(directory):
        print(filename.name)
        count_list = single_file_redaction(directory, filename.name, directory_output, audit_log_name)
        with open(os.path.join(str(audit_log_name)), 'a') as file_audit_log:
            file_audit_log.write('File Processed: ' + str(filename.name) + ', ' + 'Total Lines ' + str(count_list[0]) +
                                 ', ' + 'Total Faulty Lines: ' + str(count_list[1]) + '\n')


if __name__ == "__main__":
    main()
