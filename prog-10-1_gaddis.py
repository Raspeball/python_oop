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
        self.sideup = "Heads"

    
    # toss method generates random number in range 0, 1
    # 0 sets sideup to "Heads"
    # otherwise sideup is set to "Tails"

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"
    
    def get_sideup(self):
        return self.sideup

    