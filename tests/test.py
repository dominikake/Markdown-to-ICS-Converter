import re  # Import the regular expression module

# Count 'Date:' items in the Markdown file
markdown_count = 0

with open('events.md', 'r') as markdown_file:
    lines = markdown_file.readlines()

for line in lines:
    if line.strip().startswith("Date:"):
        markdown_count += 1

# Count '{number:}' items in the text file
text_count = 0

with open('ccs_events.txt', 'r') as text_file:
    lines = text_file.readlines()

# Define a regular expression pattern to match '{number:}'
pattern = r'\d+:'

for line in lines:
    # Use re.search to find the pattern in each line
    if re.search(pattern, line):
        text_count += 1


# Create a test to compare the two values
if markdown_count == text_count:
    print("Test passed: The counts match.")
else:
    print("Test failed: The counts do not match.")

# Print the counts for verification
print(f"Markdown count: {markdown_count}")
print(f"Text count: {text_count}")