'''while True:
    try:
        a=int(input("Enter number 1.\n"))
        b=int(input("Enter number 2.\n"))
        print(f"The sum is {a/b}")
    except ValueError:
        print("Please don't write string.")

    except ZeroDivisionError:
        print("Hey don't divide by zero.")


    except Exception as e:
        print("Some error occured!",e)'''
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older!")
    return "Access granted."

try:
  print(check_age(20))  # Access granted.
  print(check_age(16))  # Raises ValueError
except ValueError as e:
  print(f"Error: {e}")