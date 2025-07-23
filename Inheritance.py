#Inheritance Ideas and example

# new class -subclass (child class or derived class)

#syntax



#def a superclass

'''class super_class:
    # attributes and methods 
    

#Inheritance
class sub_class(super_class):
# attributes and methods of super_class
# attributes and methods of sub_class'''




'''#superclass
class Animal:
    
    name = ""
    
    def eat(self):
        print('Hey Eat food!')
        
#subclass dog
class Dog(Animal):
    
    
    def eat(self):
        print('Hey Eat food now!')
    
    #new method in subclass 
    def display(self):
        print("My name is", self.name) #inhertance of super class method
        
        
#create an obj from subclass
mountain = Dog()


mountain.name = "Mister"
mountain.eat()


#call subclass method
mountain.display()'''



a = 5
'''sdsdsdsd'''
a = 10  # overrides that method or function or message 


#Method Overriding



# trying to access the supercalss method 


#uisng super() function to access the superclass method in overriding !!!
class Animal:
    
    name = ""
    
    def eat(self):
        print('Hey Eat food! i am from super class')
        
#subclass dog
class Dog(Animal):
    
    
    def eat(self):
        super().eat() # to access the method from superclass
        print('Hey Eat food now! i am from subclass')
    
    #new method in subclass 
    '''def display(self):
        print("My name is", self.name) #inhertance of super class method'''
        
        
#create an obj from subclass
mountain = Dog()


mountain.name = "Mister"
mountain.eat()


#call subclass method
# mountain.display()





