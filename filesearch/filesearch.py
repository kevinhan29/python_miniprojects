"""
Write a script that searches a folder you specify (as well as all its subfolders) on your computer
and compiles a list of all .jpg files. The list should contain the complete path of each .jpg file.

If you are feeling bold, create a list containing each type of file extension you find in the folder.

Start with a small folder to make it easy to check whether your program is working correctly.
Then switch that small folder name with a bigger folder.

This program should work for any specified folder on your computer.
"""
import os

# function definitions
def getExtension(name: str) -> str:
    """ gets file extension of a file name """
    try:
        index = name.rindex(".")            # find right-most "." which serves as file extension delimiter
    except:
        return None
    return name[index:]

# global variables
file_path = "/Users/kevinhan/Pictures"       # file path to search
jpg_files = []                                # list of all jpg/jpeg files
file_extensions = {}                          # all file extension types in each dir. Key -> Dir, List of extensions -> Value

# get all dir path (string), dir names (list of strings), and file names (list of strings)
for dir_path, dir_names, file_names in os.walk(file_path):
    file_extensions[dir_path] = []          # create key:value pair for current dir.  Val = list of extensions
    for file in file_names:
        if getExtension(file) == None:      # move onto the next file if current file has no extension
            continue
        temp_extension = getExtension(file).lower()

        # add jpg/jpeg files to jpg_files list
        if temp_extension == ".jpg" or temp_extension == ".jpeg":
            jpg_files.append(dir_path + file)

        # create list of unique file extensions in current dir_path
        if file_extensions[dir_path].count(temp_extension) == 0:    # if current file extension doesn't exist, add to list
            file_extensions[dir_path].append(temp_extension)

# print out results
print(f"All of the jpg/jpeg files in {file_path} and its sub directories are: ")
for file in jpg_files:
    print(file)

for path, extensions in file_extensions.items():
    print(f"\nAll of the file extensions in {path} are: ")
    for ext in extensions:
        print(f"{ext}    ", end="")
    print("")