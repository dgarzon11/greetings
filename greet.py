# greet.py
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the date into the desired format
date_string = now.strftime("%d/%m/%Y %H:%M:%S")

# Define the greeting message
greeting = f"Good morning! Today is {date_string}\n"

# Filename where the greetings will be saved
filename = "greetings.txt"

# Open the file in append mode ('a') so it won't overwrite previous greetings
with open(filename, 'a') as file:
    file.write(greeting)

print(f"Greeting added to {filename}")
