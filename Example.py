#def a class named person

class Person:
    
    #construtor method that runs when object gets created
    def __init__(self, name, age):
        self.name = name # setting the name attribute
        self.age = age # setting the age attribute
        
    def welcome(self):
        return f"Hello, i am {self.name} and my age is {self.age}."
    
#create an obj
per1 = Person("Alex", 25)


#calling the method
print(per1.welcome())



#Constructor is used automatically when we create an object from a class

# it initialises the attributes.
#we can also pass the value directly into the object 
#without constructor, manually assigning every variable after the object is created.....


        