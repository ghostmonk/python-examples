import sys

file_name = 'misc/errors.txt'

try:
    with open(file_name, 'x') as a_file:
        a_file.write('Meatballs\n')
except:
    print(f"The file {file_name} already exists!!")

