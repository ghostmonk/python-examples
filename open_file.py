new_file = open('misc/edit_me.txt', 'w+')
new_file.write('The rain in spain falls mainly on the plains\n')
new_file.write('There once was a man from Nantucket\n')
new_file.writelines([
    'The corners are the hot spots full of mad criminals\n',
    'I am the master of my fate, I am the captain of my soul\n',
    'He wore his gun outside his pants, for all the honest world to see\n',
])
new_file.close()

