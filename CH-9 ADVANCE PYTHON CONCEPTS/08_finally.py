def divide(a,b):
    try:
        c=a/b
        print(c)
    except Exception as e:
        print(e)
        return None
    finally:
        print("This code will run everytime.")


a=int(input("Enter number 1.\n"))
b=int(input("Enter number 2.\n"))
divide(a,b)