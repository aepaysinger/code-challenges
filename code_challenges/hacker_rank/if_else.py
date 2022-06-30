import math
import os
import random
import re
import sys


def weird_stuff(n):
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and n in range(2,6):
        print("Not Weird")
    elif n % 2 == 0 and n in range(6,21):    
        print("Weird")
    elif  n % 2 == 0 and n > 20:
        print("Not Weird") 
 #make a test for each result