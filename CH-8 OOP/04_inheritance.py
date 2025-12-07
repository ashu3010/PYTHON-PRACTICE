class Animal:  # Parent class (superclass)
    location= "Australia"
    def __init__(self, name):
        self.name = name
    def name(self):
        return self.name
    def speak(self):
        print("Generic animal sound")
class dog(Animal):
    def speak(self):
        super().speak() # It uses this function from parent class.
        print("Woof")
    
# jack=Animal("Dog")
# print(jack.name)
# jack.speak()

d= dog("Ginger")
d.speak()
print(d.name)

