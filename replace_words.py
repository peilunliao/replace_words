import os

# Assuming the file 'data.txt' is in the same directory as the script
data_file = os.path.join(os.path.dirname(__file__), 'changelist.txt')


def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def write_file(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(lines)

def read_changelist(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    file1, file2 = lines[0].strip().split(',')
    changelist = []

    # Parse the second line for changelist
    segments = lines[1].strip().split(',')
    for segment in segments:
        if '-' in segment:
            start, end = map(int, segment.split('-'))
            changelist.extend(range(start - 1, end))  # Convert to zero-based index
        else:
            changelist.append(int(segment) - 1)  # Convert to zero-based index

    return file1, file2, changelist

def main():
    changelist_file = "changelist.txt"
    file1, file2, changelist = read_changelist(changelist_file)

    # Read file contents
    file1_lines = read_file(file1)
    file2_lines = read_file(file2)

    # Create a copy of file1_lines to write to newfile.txt
    newfile_lines = list(file1_lines)

    # Replace lines in newfile_lines with lines from file2 based on changelist
    for line_num in changelist:
        if 0 <= line_num < len(file1_lines) and line_num < len(file2_lines):
            newfile_lines[line_num] = file2_lines[line_num]

    # Write the updated content to newfile.txt
    write_file("newfile.txt", newfile_lines)

    print("New file 'newfile.txt' has been created based on changelist.")

if __name__ == "__main__":
    main()
