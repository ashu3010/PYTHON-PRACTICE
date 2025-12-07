class Employee:
    def __init__(self,salary, name, bond=1):
        self.salary=salary #Create an instance attribute of name salary and assign it with salary
        self.name=name
        self.bond=bond
        
        pass
    def bond(self):
        return self.bond
    def get_info(self):
       return (f"The name of the Employee is {self.name}.\nHis salary is {self.salary}.\nThe bond is for {self.bond} years.")
        
        
ashu=Employee(100000,"ASHUTOSH SINGH",4)
print(ashu.get_info())
print(ashu.bond)


