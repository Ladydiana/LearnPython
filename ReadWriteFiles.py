# -*- coding: utf-8 -*-
"""
READING & WRITING A FILE
"""

"""
f = open('my_path/my_file.txt', 'r')
file_data = f.read()
f.close()

f = open('my_path/my_file.txt', 'w')
f.write("Hello there!")
f.close()

with open('my_path/my_file.txt', 'r') as f:
    file_data = f.read()
#with allows you to open a file, do operations on it, and automatically close it 
#after the indented code is executedw, so we don’t have to call f.close()! 
#!!! But you can only access the file object, f, within the indented block.
"""

with open("camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())
    
camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)


def create_cast_list(filename):
    cast_list = []
    with open("flying_circus_cast.txt") as f:
        for line in f:
            cast_list.append(line.strip().split(',')[0])
    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)