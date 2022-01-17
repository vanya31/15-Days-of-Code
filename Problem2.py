#Problem Statement:
#Two cats and a mouse are at various positions on a line. You will be given their starting positions.
#Your task is to determine which cat will reach the mouse first, assuming the mouse does not move and the 
# cats travel at equal speed. If the cats arrive at the same time, the mouse will be allowed to move and
#  it will escape while they fight.
#You are given  queries in the form of , , and  representing the respective positions for cats  and , and for mouse . 
# Complete the function  to return the appropriate answer to each query, which will be printed on a new line.
#If cat  catches the mouse first, print Cat A.
#If cat  catches the mouse first, print Cat B.
#If both cats reach the mouse at the same time, print Mouse C as the two cats fight and mouse escapes.

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if (abs(z-y)==abs(z-x)):
        return "Mouse C"
    elif (abs(z-y)>abs(z-x)):
        return "Cat A"
    elif (abs(z-y)<abs(z-x)):
        return "Cat B"
    
    q = int(input())
    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)
        print(result)

        
