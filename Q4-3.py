# Use a while loop to reverse a given number (e.g., 123 → 321).

game=int(input("Enter a number\n"))
if(game>9):
       print("no. is not valid for reveersing")
    
while(game>9):
     

    print(int(str(game)[::-1]))
    break
       
print("no. is not valid for reveersing")
