# Class: Think of a class as a blueprint or a template. It defines what an object will be like – what data it will hold and what actions it can perform. It doesn't create the object itself, just the instructions for creating it. It's like an architectural plan for a house.

# Object (Instance): An object is a specific instance created from the class blueprint. If "Car" is the class, then your red Honda Civic is an object (an instance) of the "Car" class. Each object has its own unique set of data. It's like the actual house built from the architectural plan.

class Employee:
    company='HP'
    def get_salary(self):# self is important here because self is a way to reference the objest of the class which is being created.
        print(self)
        return 100000
ashu=Employee()
print(ashu.company)
print(ashu.get_salary())


abhi=Employee()
print(abhi.company)