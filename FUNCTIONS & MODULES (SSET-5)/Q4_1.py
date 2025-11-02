# Write a recursive function factorial(n) that returns the factorial of a number.

def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)
n=int(input("Enter the no. for factorial.\n"))

print(factorial(n))
