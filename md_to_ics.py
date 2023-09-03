from ics import Calendar, Event
from datetime import datetime

# Read the Markdown file
with open('events.md', 'r') as markdown_file:
    markdown_text = markdown_file.readlines()

# Create an ICS calendar
cal = Calendar()

event_title = ""
event_date = ""

for line in markdown_text:
    line = line.strip()
    if line.startswith("# "):
        # Create an event for the previous event title and date
        if event_title and event_date:
            event = Event()
            event.name = event_title
            event_date = event_date.replace(",", "").strip()
            event_datetime = datetime.strptime(event_date, '%B %d %Y')
            event.begin = event_datetime
            cal.events.add(event)
        
        # Extract the new event title
        event_title = line.lstrip("# ")
    elif line.startswith("Date: "):
        # Extract the event date
        event_date = line.replace("Date: ", "")

# Create an event for the last event in the file
if event_title and event_date:
    event = Event()
    event.name = event_title
    event_date = event_date.replace(",", "").strip()
    event_datetime = datetime.strptime(event_date, '%B %d %Y')
    event.begin = event_datetime
    cal.events.add(event)

# Save the ICS file
with open('school_calendar.ics', 'w') as ics_file:
    ics_file.writelines(cal)
