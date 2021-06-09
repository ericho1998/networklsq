# Network Analysis - Angles and Distances Least Squares Estimation: Conversion from C++ to Python
# Based off Lab 1 from ENGO 563
# Eric Ho
# June 9th, 2021
import numpy as np
import math as m
import functions as f

def main():
    obs = np.loadtxt(open('obs.txt', 'r'), delimiter=' ', dtype=[('type', 'U10'),('value', 'f4'),('mfrom', 'i1'),('mto', 'i1'),('mat', 'i1')])
    coords = np.loadtxt(open('coords.txt', 'r'), delimiter=' ', dtype =[('point', 'i1'), ('easting', 'f4'),('northing', 'f4'),('known', 'U10')])
    u1 = coords['known']
    cl = np.loadtxt(open('cl.txt','r'), delimiter=' ')
    u = f.unknowns(u1)
    u = int(u)
    A = np.zeros((np.size(obs,0), u))


if __name__ == '__main__':
    main()
