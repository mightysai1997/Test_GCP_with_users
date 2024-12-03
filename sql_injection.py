import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# User input (could come from a form, URL parameter, etc.)
username = input("Enter username: ")
password = input("Enter password: ")

# Vulnerable query: directly inserting user input into the SQL statement
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

# Execute the query
cursor.execute(query)

# Fetch results
user = cursor.fetchone()

if user:
    print("Login successful!")
else:
    print("Invalid username or password.")

# Close the connection
conn.close()
