import sys

file_name = 'misc/errors.txt'

try:
    with open(file_name, 'x') as a_file:
        a_file.write('Meatballs\n')
except FileExistsError as err:
    print(f"The file {file_name} already exists!!")
    sys.exit(1)
except:
    print(f"Unable to write to file")
    sys.exit(1)
else:
    print(f"Write to {file_name}")
finally:
    print("Execution complete")

