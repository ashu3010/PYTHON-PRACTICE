# write to a file called John doe.txt
# It should contain data about John Doe

f=open("John Doe.txt","a")

string ='''
John Doe initially lived in Phoenix, Arizona. 
He is a very nice guy
'''


f.write(string)
f.close()


