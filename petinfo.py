# Programming exercise 1 chapter 10
# "Starting out with Python" by Tony Gaddis
# Pearson, 4th edition, Global Edition
#
#
#
### --- Program --- ###
#
class Pet:
    def __init__(self, nme, anm_type, ag):
        self.__name = nme
        self.__animal_type = anm_type
        self.__age = ag

    def set_name(self, nme):
        self.__name = nme
    
    def set_animal_type(self, anm_type):
        self.__animal_type = anm_type
    
    def set_age(self, ag):
        self.__age = ag
    
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age
    
    def __str__(self):
        stat = f"{self.__name} is a {self.__age} year old {self.__animal_type}"
        return stat
