# Read the input .txt file
with open('school_events.txt', 'r') as txt_file:
    lines = txt_file.readlines()

markdown_events = []

i = 0
while i < len(lines):
    # Read the month and year
    month_year = lines[i].strip().split()
    if len(month_year) != 2:
        # Invalid format for month and year, skip this section
        i += 1
        continue

    month = month_year[0].upper()
    year = month_year[1]
    i += 1

    while i < len(lines) and ':' in lines[i]:
        # Read the day and event name
        day_event = lines[i].strip().split(': ')
        if len(day_event) != 2:
            # Invalid format for day and event name, skip this line
            i += 1
            continue

        day = day_event[0]
        event_name = day_event[1]

        # Format the date
        formatted_date = f"{month} {day}, {year}"

        # Create the Markdown event entry
        markdown_event = f"# {event_name}\nDate: {formatted_date}\n"
        markdown_events.append(markdown_event)

        i += 1

# Write the Markdown output to a new file
with open('events.md', 'w') as output_file:
    output_file.writelines(markdown_events)
    print('Events parsed successfully!')
