def sum(*num):
    total=0
    for values in num:
        total+=values
    return total
print(sum(232,4,122,12,423))



##########################################################################


def my_function(*args):
    print(type(args))  # <class 'tuple'>
    for arg in args:
        print(arg)

my_function(1, 2, 3, "hello")  # Output: 1 2 3 hello
my_function()  # No output (empty tuple)
my_function("a", "b")  # Output: a b