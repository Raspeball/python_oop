# Program 10-1 (p. 517) from
# "Starting out with Python" by Tony Gaddis
# Pearson, 4th edition, Global Edition
#
#
#
### --- Code --- ###
#
import random
# Coin class simulates a coin that can be flipped

class Coin:

    # initialize sideup data attr with "Heads"
    def __init__(self):
        self.__sideup = "Heads" #private attr

    
    # toss method generates random number in range 0, 1
    # 0 sets sideup to "Heads"
    # otherwise sideup is set to "Tails"

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"
    
    def get_sideup(self):
        return self.__sideup

#
# Testing
def main():
    my_coin = Coin()

    print(f"{my_coin.get_sideup()} is the side that is up")

    print("The coin is tossed...")
    my_coin.toss()

    print(f"{my_coin.get_sideup()} is the side that is up")
    #
#
main()
    