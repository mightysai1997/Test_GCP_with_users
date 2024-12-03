import os

# User input is used to build file paths
filename = input("Enter the file name: ")
with open(f"/uploads/{filename}", "r") as f:
    print(f.read())
