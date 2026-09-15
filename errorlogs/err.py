import random

error_messages = [
    "Error: Unable to connect to database",
    "Warning: Failed password for root",
    "Fatal error: Out of memory",
    "Syntax error, unexpected T_VARIABLE",
    "Error: Could not open input file: script.php",
    "Fatal error: Call to undefined function myFunction()",
    "cybercamp{your_flag_here}",
    "Error: Could not establish secure connection",
    "Error: Missing required field: name",
    "Syntax error, unexpected T_ENCAPSED_AND_WHITESPACE, expecting T_STRING or T_VARIABLE or T_NUM_STRING",
]

with open("error_log.txt", "w") as f:
    for _ in range(1000):  # Change this number to generate a longer or shorter log file
        # Randomly select an error message
        message = random.choice(error_messages)
        
        # Write the error message to the log file
        f.write(message + "\n")

print("Log file created successfully.")

