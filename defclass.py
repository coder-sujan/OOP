#here we  learn to define the class

#syntax
# class ClassName:
    #provide class description
    
'''class Bike: # Bike is the name of the class
    name: "abc" #variables with some values
    gear = 0'''
    #the variables created inside the class are called attributes.
    
    
    
#objects

#so object is called an instance of class

#example

#syntax of object
#objectName = ClassName()


class Bike: # Bike is the name of the class
    name = "null" #variables with some values
    gear = 10
    #the variables created inside the class are called attributes.

#object of the class
bike1 = Bike() #bike1 is the obj of the class called Bike()
#after creating this object of the class, access the class attributes.


#Example
#Accessing the class Attributes Using Objects

#trying to access name propetry (attributes)
bike1.name = "Mountain Bike"
#accessing the 2nd attribute of the class
bike1.gear = 5

print(f'Name: {bike1.name}, Gear: {bike1.gear}')



#define a class
#create attributes
#create object of the class (two objects)
#access the attributes and even modify it (. notation)


class Dog:
    pass

d1 = Dog()
d1.name ="aa"
d1.breed = "ab"


print(d1.name)

#using the above constructor with above example

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
d1 = Dog("AA1", 'AB1')


print(d1.name)
print(d1.breed)



        
    

  

  