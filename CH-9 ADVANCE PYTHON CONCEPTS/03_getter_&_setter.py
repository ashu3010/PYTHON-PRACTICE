'''class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @property
    def first_name(self):
        l= self.name.split(" ")
        print(l)
        return f"First name was ({l[0]})"
    @first_name.setter
    def first_name(self,first):
        l= self.name.split(" ")
        new_name=f"{first} {l[1]}"
        self.name=new_name
    

e=Employee("Drake Russule",34000)



print(e.first_name)

e.first_name="Jason"
print(e.name)

# e.lifecycle=20
# print(e.lifecycle)'''

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):  # Read-only computed property
        return 3.1416 * self._radius * self._radius

c = Circle(5)
print(c.radius)  # 5
print(c.area)  # 78.54

# c.radius = 10  # Raises AttributeError: can't set attribute
# c.area = 20 # Raises AttributeError: can't set attribute