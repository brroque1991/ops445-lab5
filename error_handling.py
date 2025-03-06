#!/usr/bin/env python3

def handle_type_error():
    try:
        print('5' + 10)
    except TypeError:
        print('At least one of the values is NOT an integer')


def handle_file_not_found_error():
    try:
        f = open('filethatdoesnotexist', 'r')
        f.write('hello world\n')
        f.close()
    except FileNotFoundError:
        print('No file found')


def handle_multiple_errors():
    try:
        f = open('filethatdoesnotexist', 'r')
        f.write('hello world\n')
        f.close()
    except (FileNotFoundError, PermissionError, IsADirectoryError):
        print('Failed to open file')


def handle_separate_errors():
    try:
        f = open('filethatdoesnotexist', 'r')
        f.write('hello world\n')
        f.close()
    except FileNotFoundError:
        print('File does not exist')
    except PermissionError:
        print('Wrong permissions')
    except IsADirectoryError:
        print('File is a directory')
    except OSError:
        print('Unable to open file')
    except Exception as e:
        print(f'Unknown error occurred: {e}')
        raise


if __name__ == '__main__':
    print("Handling TypeError:")
    handle_type_error()

    print("\nHandling FileNotFoundError:")
    handle_file_not_found_error()

    print("\nHandling Multiple Errors:")
    handle_multiple_errors()

    print("\nHandling Separate Errors:")
    handle_separate_errors()