# Create a program that checks if a person is eligible to vote (age >= 18).
age= int(input("What is your age?\n"))

if(age<=0):
    print("this is not your age.")
elif(age<18):
    print("You are not eligible for voting now.\nTry again after"+ str(age-18)+ "years.")
else:
    print("You are eligible for voting.")
    


