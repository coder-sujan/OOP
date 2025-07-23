#Multiple Inheritance

'''class supercalss1:
    #feats of supercalss1
    
class superclass2:
    #feats of supercalss2
    
class MultiDerivedIdeas(supercalss1, superclass2):
    #feats of supercalss1 + #feats of supercalss2 = #feats of MultiDerivedClass'''
    
    



#example:

class Mammal:
    def mam_info(self):
        print('Hey i am Mammal method')
        
class wingedAnimal:
    def winged_ani(self):
        print('I believe i can fly!')
        
class Bat(Mammal, wingedAnimal):
    pass


#create obj

b1 = Bat()


b1.mam_info()
b1.winged_ani()



#wap using inheritance and multi inheritenace 