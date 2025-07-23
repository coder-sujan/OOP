#Encapsulation Example

#hiding or protecting variables but can still access the function and outputs...


'''class WaterBottle:
    def __init__(self):
        self.__water__level = 0 # no direct access outside of the class
    
    #fill water method
    def fill(self, amount):
        if amount > 0:
            self.__water__level += amount
            print(f'Filled  {amount}ml of water')
        else:
            print('Invalid amount !!')
    
    #drink method
    def drink(self, amount):
        if 0 < amount <=self.__water__level:
            self.__water__level -= amount
            print(f'Drank {amount}ml of water.')
        else:
            print('Not enough')
        
             
    def check(self):
        return f'current water level: {self.__water__level} ml'
    
    
#obj creation
bottle = WaterBottle()

bottle.fill(500)
print(bottle.check())


bottle.drink(100)
print(bottle.check())


print(bottle.__water__level)'''


        
        
        
        
# example

class Counter:
    def __init__(self):
        self.__count = 0 #private
        
    def increase(self):
        self.__count += 1 # increasing the value also using safe way...
        
    def get_count(self):
        return self.__count #safely returing the count 
    
#obj    
c = Counter()

c.increase() #increase the count by 1
c.increase() #increase again
c.increase() #increase again
c.increase() #increase again


# print(c.get_count()) 
print(c.__count)
        
            
        
