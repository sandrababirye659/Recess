# Write a program to handle errors.The program should ask for two numbers using input and then
# divides them. Use an infinite loop to keep asking until a valid input is provided.

while True:
    try:
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))
        result = num1 / num2
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a non-zero second number.")
    else:
        print("The result of the division is: ",result)
        break