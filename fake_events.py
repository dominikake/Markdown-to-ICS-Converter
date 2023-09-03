from faker import Faker
import random

# Initialize the Faker generator
fake = Faker()

# Open the file for writing
with open('school_events.txt', 'w') as file:
    # Generate events for September
    file.write('SEPTEMBER 2023\n')
    for _ in range(4):
        day = random.randint(1, 30)  # Generate a random day for September
        event_name = fake.sentence(nb_words=4)  # Generate a random event name
        file.write(f"{day}: {event_name}\n")

    # Generate events for October
    file.write('\nOCTOBER 2023\n')
    for _ in range(6):
        day = random.randint(1, 31)  # Generate a random day for October
        event_name = fake.sentence(nb_words=4)  # Generate a random event name
        file.write(f"{day}: {event_name}\n")
