with open('misc/edit_me.txt', 'w+') as new_file:
    new_file.write('The rain in spain falls mainly on the plains\n')
    new_file.write('There once was a man from Nantucket\n')
    new_file.writelines([
        'The corners are the hot spots full of mad criminals\n',
        'I am the master of my fate, I am the captain of my soul\n',
        'He wore his gun outside his pants, for all the honest world to see\n',
    ])


with open('misc/edit_me.txt', 'r') as new_file:
    print(new_file.read())
    new_file.seek(0)

    print("READ AGAIN\n") 
    print(new_file.read())

