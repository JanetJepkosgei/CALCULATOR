print("Welcome to the Fancy Calculator")
print("\n")

# user input
num1 = float(input("Enter the first number: "))
operation = input("Enter Operation(+,-,*,/): ")
num2 = float(input("Enter the second number: "))

# the actual calculation
if operation =="+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation =="-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation =="*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation =="/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid  operation entered.")
