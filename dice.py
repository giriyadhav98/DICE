
import random
import time

import dice as dice

print ("\n rooling the dice...")
time.sleep (1)

dice = random.randint (1, 6)

print ("the values are:")
print ("Dice =", dice)

roll_again = input ("\n Roll the dice again? (Y/N) ")
if (roll_again == 'Y'):
    print ("the values are:")
    print ("Dice =", dice)
else:
    print('exited')
