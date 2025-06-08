# Programming exercise 1 chapter 10
# "Starting out with Python" by Tony Gaddis
# Pearson, 4th edition, Global Edition
#
#
#
### --- Program --- ###
#
class Pet:
    def __init__(self, nme, type, ag):
        self.__name = nme
        self.__animal_type = type
        self.__age = ag

    def set_name(self, nme):
        self.__name = nme
    
    def set_animal_type(self, type):
        self.__animal_type = type
    
    def set_age(self, ag):
        self.__age = ag
    
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age
