# Vulnerable login system
username = input("Username: ")
password = input("Password: ")

# Check if credentials match
if username == "admin" and password == "admin":
    print("Welcome!")
else:
    print("Invalid credentials!")
