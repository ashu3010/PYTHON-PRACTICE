# Print the multiplication table of a number (entered by user).
n= int(input("Say the number and get the table.\n"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)