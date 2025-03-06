#!/usr/bin/env python3
import lab5b

file1 = 'seneca1.txt'
file2 = 'seneca2.txt'
file3 = 'seneca3.txt'
string1 = 'First Line\nSecond Line\nThird Line\n'
list1 = ['Line 1', 'Line 2', 'Line 3']

lab5b.append_file_string(file1, string1)
print(lab5b.read_file_string(file1))
print(lab5b.read_file_list(file1))

lab5b.write_file_list(file2, list1)
print(lab5b.read_file_string(file2))

lab5b.copy_file_add_line_numbers(file2, file3)
print(lab5b.read_file_string(file3))