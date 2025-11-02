# Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

# Both length and width


def calculate_area(length, width=10):
    return (length*width)
length=int(input("Enter length of rectangle.\n"))
width=int(input("Enter width of rectangle.\n"))
print(calculate_area(length,width))

# Only length (use default width)

print(calculate_area(length))
