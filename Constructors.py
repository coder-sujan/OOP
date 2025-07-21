#constructors 

'''class Bike:
    name = ""
    
#create some objts
bike1 = Bike()

#-----------------------#

class Bike:
    
    #creating a constructors  (special method that runs auto when an object is called)
    def __init__(self, name = ""):
        self.name = name
        
        
#object
bike1 = Bike()
bike1 = Bike('Mountain Bike')'''


#example 2


class Student:
    def __init__(self, name):
        self.name = name  #sets name during the object creation
        

s = Student("Tom")
print(s.name)
        


        
    
    
