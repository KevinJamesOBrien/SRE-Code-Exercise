import os
import datetime
"""
Comments added here between three "s
https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/
"""
directory = 'SampleFiles'
filename = 'SampleFile.txt'

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
datetime = datetime.datetime.now()
auditLogName = 'LOG REDACTION AUDIT LOG - ' + str(datetime)
with open(os.path.join(str(directory), str(auditLogName)) 'a') as file_audit_log:
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
            print('Total Lines: ' + str(lineCount))
            print('Total Faulty Lines: ' + str(lineCountFaulty))
            break
        lineCount += 1
        print('Line: ' + str(lineCount) + ' processed.')
