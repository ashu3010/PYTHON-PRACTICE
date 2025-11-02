# Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.

def multiply(a, b):
    '''
    Multiply two numbers.

    parameters:
    a(int / float)= 1st number.
    b(int/ float)= 2nd numbrer.

    Returns:
    product of a and b.
    '''
    return a*b
print(multiply(3,5))
print(multiply(347,5))
print(multiply(3,12))
help(multiply)