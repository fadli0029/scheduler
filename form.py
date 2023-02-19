import os
import sys

form_data = sys.stdin.read()

# Extract the name and age from the form data
name = ""
age = ""
for line in form_data.split("\n"):
    if "name=" in line:
        name = line.split("=")[1]
    if "age=" in line:
        age = line.split("=")[1]

# Write the form data to a table in a new markdown file
with open("docs/table.md", "a") as f:
    f.write(f"| {name} | {age} |\n")
