'''
Write a program that keeps asking the user to enter a password until they enter the correct one.
'''
key = "ashu007#"
entered_pass=input("Enter Your Password:")
while (entered_pass != key):
    entered_pass=input("Wrong password! Try again...")
print("You are logged in...")
