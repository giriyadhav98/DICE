import random
import time

roll_again = "yes"

while roll_again == "y" :
    print ("\n rooling the dice...")
    time.sleep (1)

    dice = random.randint (1, 6)

    print ("the values are:")
    print ("Dice =", dice)

    roll_again = input ("\n Roll the dice again? (Y/N) ")

