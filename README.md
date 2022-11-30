# Solution
This python script is meant to run through any number of .gz files, only processing .gz files within the 
input files directory, ignoring all other files and folders.
All .gz files are then processed line by line in byte format to check the validity of the line. 
All valid lines are re-written into a text file which is subsequently compressed into a .gz file once fully rewritten
An audit log is also created with the below requirements in the same folder as the python script.

# Assumptions 
This python script assumes that there already exists a folder that contains the input files, and an empty folder
that will contain the output files. These are configurable as parameters at the top of "LogRedaction.py".
This program also assumes that you are on Python 3.10+ (testing failed on 3.6, but it may be compatible in between)

# Prepare and Run
1. Put all files to be processed inside the input folder.
2. Create an empty folder to hold the output files.
3. Edit the "LogRedaction.py" file global variables at the top to point to the right directories for input and output 
4. Run "LogRedaction.py". Output files will be processed and archived into a sub folder in the output folder based
on the same datetimestamp as the audit log. 

# NB
See Readme_Assignment.md for assignment details 