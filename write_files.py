# Open a non-existent data file for writing
f = open('file1.txt', 'w')

# Add lines of text to the file
f.write('Line 1\nLine 2 is a little longer\nLine 3 is too\n')

# Close the file
f.close()

# Open a new file for writing
f = open('file2.txt', 'w')
f.write('Line 1\nLine 2 is a little longer\nLine 3 is as well\n')
f.write('This is the 4th line\n')
f.write('Last line in file\n')
f.close()

# Open the file for appending (this will not erase existing content)
f = open('file2.txt', 'a')
f.write('Adding a new line without erasing existing content\n')
f.close()

# Open the file for appending
f = open('file1.txt', 'a')
f.write('This is the 4th line\n')
f.write('Last line in file\n')
f.close()

my_number = 1000
my_list = [1, 2, 3, 4, 5]
f = open('file3.txt', 'w')
f.write(str(my_number) + '\n')
for num in my_list:
    f.write(str(num) + '\n')
f.close()