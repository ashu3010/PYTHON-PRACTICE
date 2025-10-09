# Write a program using match case that simulates a simple calculator.
# 1)Ask the user for two numbers and an operation (+, -, *, /).
# 2)Perform the operation using match case.

num1=int(input("Enter 1st no. :"))
num2=int(input("Enter 2nd no. :"))

operation=input("Enter your operation:")

match operation:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)