# Step 1: Create a text file named data.txt with the following content:
# Hello World
# This is the second line
# Third line
# Last line

# Step 2: Open the file and read its contents
f = open('/Users/bryanrossroque/ops445/lab5/data.txt', 'r')
read_data = f.read()
print("Contents of the file using read():")
print(read_data)
f.close()

# Step 3: Split the contents into a list of lines
list_of_lines = read_data.split('\n')
print("\nContents of the file as a list of lines:")
print(list_of_lines)

# Step 4: Alternative methods to read lines into a list

# Method 1: Using list(f)
f = open('/Users/bryanrossroque/ops445/lab5/data.txt', 'r')
method1 = list(f)
f.close()
print("\nContents of the file using list(f):")
print(method1)

# Method 2: Using f.readlines()
f = open('/Users/bryanrossroque/ops445/lab5/data.txt', 'r')
method2 = f.readlines()
f.close()
print("\nContents of the file using f.readlines():")
print(method2)

# Optional: Using 'with' statement for better practice
print("\nUsing 'with' statement:")
try:
    with open('/Users/bryanrossroque/ops445/lab5/data.txt', 'r') as f:
        read_data_with = f.read()
        print(read_data_with)
except FileNotFoundError:
    print("The file does not exist.")