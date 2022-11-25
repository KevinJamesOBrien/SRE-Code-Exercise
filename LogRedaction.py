import os
"""
Comments added here between three "s
https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/
"""
directory = 'SampleFiles'

for filename in os.scandir(directory):
    print(filename.name)

print("Hello World")
