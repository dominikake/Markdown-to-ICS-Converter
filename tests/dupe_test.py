# Define the path to your text file
file_path = 'ccs_events.txt'

# Create a set to store unique lines
unique_lines = set()

# Create a list to store duplicated lines
duplicated_lines = []

# Read the file and check for duplicates
with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()  # Remove leading/trailing whitespace
        if line in unique_lines:
            duplicated_lines.append(line)
        else:
            unique_lines.add(line)

# Check if there are duplicated lines
if duplicated_lines:
    print("Duplicated lines found:")
    for line in duplicated_lines:
        print(line)
else:
    print("No duplicated lines found.")
