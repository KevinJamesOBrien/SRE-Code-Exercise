# SRE-Code-Exercise: Log Redaction
# Scenario
One of our customers has been inadvertently uploading sensitive personally-identifying information (PII) to our system 
over a period of several months. The customer has since realized their mistake and removed the data from the system, 
but some of that information was reflected in debugging logs enabled on the system and will need it to be removed. 
The logs in question are archived to a central location and compressed with the gzip utility.
# Scope/Assumptions
We are only concerned with the archived logs. Backups, application data and any other storage locations 
may assumed to have been addressed separately. You may assume that each line of each input log file contains data 
from one and only one customer record. All relevant log files may assumed to be local to the script being run 
(i.e. located on the same system)
# Requirements
1. The solution must accept as input one or more text logfiles that have been compressed with the gzip algorithm.
2. For each input file, the solution must produce a redacted copy of the file that has been compressed 
with the gzip algorithm.
3. The solution must also create an audit log that includes the name of each file processed, a count of the total 
number of lines processed in each log file, and a count of the total number of lines removed from each log file. 
The audit log may additionally contain any other information you feel is pertinent. The audit log must not contain 
any information from the removed lines.
4. The solution must not alter logs in-place, as we will want to verify that they have not been corrupted before 
replacing the originals.
5. The solution must remove all loglines containing sensitive data as identified in the sample data provided.
6. The solution must contain clear code comments explaining its usage and internal operations.
7. The solution must be able to reliably process hundreds or thousands of logfiles containing 512 MiB or more of 
uncompressed log entries per file.
# Preferences
1. The ideal solution will be written in Typescript/Javascript, Python, Go/GoLang, Rust, or Bash (including associated 
UNIX CLI tools like awk, sed, etc.). However, any working code is acceptable.
2. The ideal solution will be cognizant of CPU, RAM and storage limitations and strive to use said resources 
efficiently while still processing log files as quickly as possible.
3. The ideal solution will preserve as much metadata (e.g.date/time stamps, file ownership, file permissions, etc.) 
as possible from the original log files in the redacted copies.
4. The ideal solution will be flexible enough to address similar needs in the future with minimal rework.
