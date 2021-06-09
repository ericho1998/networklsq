# Functions for the Network Least Squares Solution
# Eric Ho
# June 9th, 2021

import numpy as np
import math as m

def unknowns(u1):
    #Figure out how many unknowns are needed to solve
    c = 0
    for i in range(0, np.size(u1)):
        if u1[i] == "Unknown":
            # Increment the number of unknowns by 2 for northing and easting
            c+=2

    return c
