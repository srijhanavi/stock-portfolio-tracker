import re

# Input and output file names
input_file = "input.txt"
output_file = "output_emails.txt"

# Read input file
with open(input_file, "r") as file:
    text = file.read()

# Find all email addresses using regex
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# Write emails to output file
with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email extraction completed. Check output_emails.txt")
