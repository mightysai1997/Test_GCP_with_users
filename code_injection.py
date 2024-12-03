# Vulnerable code using eval()
user_input = input("Enter a Python expression: ")

# The code executes the user input as Python code
result = eval(user_input)

print("Result of the expression:", result)
