#def methods
#same as function but inside class - acts differently.

#create a class

class Room:
    length = 0.0
    breadth = 0.0
    
    
    #create a function (as method)
    #method to calculate the area...
    def calc_area(self):
        print("Area of Room =", self.length * self.breadth)
        

#object of the class
#study room
study_room = Room()


#assign some values to all the properties l / b

study_room.length = 41.5
study_room.breadth = 43.5


#access the method inside the class
#similar to calling the function
study_room.calc_area()


