
"""
for filename in os.scandir(directory):
    singleFileRedaction(filename)
    print(filename.name)


def singleFileRedaction(filename1):
"""
lineCount = 0
lineCountFaulty = 0
match_string = ["CC=", "SSN="]
filename_output = str(filename) + '_output.txt'
datetimenow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
auditLogName = 'LogRedactionAuditLog.' + str(datetimenow) + '.txt'
with open(os.path.join(str(directory), str(auditLogName)), 'a') as file_audit_log:
    file_audit_log.write('+++++++ LOG REDACTION AUDIT LOG - ' + str(datetimenow) + '. +++++++\n')
with open(os.path.join(str(directory), str(filename)), 'r') as file:
    print('creating output file...')
    while True:
        line = file.readline()
        # Open the output (redacted) file to append only good lines to
        with open(os.path.join(str(directory), str(filename_output)), 'a') as file_output:
            # Checks if line in file contains anything in the match_string. Writes to output file if not.
            if any(x in line for x in match_string):
                lineCountFaulty += 1
            else:
                file_output.write(line)
        if not line:
            # Logic here to write to audit log
            with open(os.path.join(str(directory), str(auditLogName)), 'a') as file_audit_log:
                file_audit_log.write('File Processed: ' + str(filename) + ', ' + 'Total Lines ' + str(lineCount) +
                                     ', ' + 'Total Faulty Lines: ' + str(lineCountFaulty) + '\n')
            print('Total Lines: ' + str(lineCount))
            print('Total Faulty Lines: ' + str(lineCountFaulty))
            break
        lineCount += 1
        print('Line: ' + str(lineCount) + ' processed.')
