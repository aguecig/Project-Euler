# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:25:43 2019

@author: aguec
"""

# project euler challenge 102
# in a file of 1000 triangles that are defined by their verticies on the 
# cartesian grid, we are to find out how many of them contain the origin in 
# their interior

# A triangle will have the origin in its interior iff:
# (i) The triangle has 4 intercepts
# (ii) Two of them are x-intercepts, and are different in sign
# (iii) Two of them are y-intercepts, and are different in sign.

import timeit
start = timeit.default_timer()
import pandas

df = pandas.read_csv('triangles.txt')

count = 0

for i in range(len(df)):
    ax = df['ax'][i]
    ay = df['ay'][i]
    bx = df['bx'][i]
    by = df['by'][i]
    cx = df['cx'][i]
    cy = df['cy'][i]    
    
    intercepts = []
    
    # pass on the case where the origin is a vertice
    if (ax == 0 and ay == 0) or (bx == 0 and by == 0) or (cx == 0 and cy == 0):
        continue
    
    # pass on the case where the origin lies on one of the line segments
    elif (ax == 0 and bx == 0) or (ax == 0 and cx == 0) or (bx == 0 and cx == 0) or (ay == 0 and by == 0) or (ay == 0 and cy == 0) or (by == 0 and cy == 0):
        continue
    
    # pass on the case where the triangle is known to be in only one half of the
    # cartesian grid
    elif (ax > 0 and bx > 0 and cx > 0) or (ay > 0 and by > 0 and cy > 0):
        continue
    
    # now do the general case
    else:
        # find the intercepts of each line segment
        
        # line segement ab
        
        # special case of vertical line
        if (bx - ax) == 0:
            xint_ab = ax
            yint_ab = 'dne'
        # special case of horizontal line
        elif (by - ay) == 0:
            yint_ab = ay
            xint_ab = 'dne'
        else:
            slope_ab = (by-ay)/(bx-ax)
            yint_ab = ay - slope_ab*ax
            xint_ab = -1*yint_ab*(1/slope_ab)
        # now search to see if either intercept is on the line segement
        if xint_ab == 'dne':
            pass
        elif (ax <= xint_ab <= bx) or (bx <= xint_ab <= ax):
            intercepts.append([xint_ab,'x'])
        if yint_ab == 'dne':
            pass
        elif (ay <= yint_ab <= by) or (by <= yint_ab <= ay):
            intercepts.append([yint_ab,'y'])
        
        # line segment ac
        
        # special case of vertical line
        if (cx - ax) == 0:
            xint_ac = ax
            yint_ac = 'dne'
        # special case of horizontal line
        elif (cy - ay) == 0:
            yint_ac = ay
            xint_ac = 'dne'
        else:
            slope_ac = (cy-ay)/(cx-ax)
            yint_ac = ay - slope_ac*ax
            xint_ac = -1*yint_ac*(1/slope_ac)
        # now search to see if either intercept is on the line segement
        if xint_ac == 'dne':
            pass
        elif (ax <= xint_ac <= cx) or (cx <= xint_ac <= ax):
            intercepts.append([xint_ac,'x'])
        if yint_ac == 'dne':
            pass
        elif (ay <= yint_ac <= cy) or (cy <= yint_ac <= ay):
            intercepts.append([yint_ac,'y'])
            
        # line segement cb
        
        # special case of vertical line
        if (bx - cx) == 0:
            xint_cb = cx
            yint_cb = 'dne'
        # special case of horizontal line
        elif (by - cy) == 0:
            yint_cb = cy
            xint_cb = 'dne'
        else:
            slope_cb = (by-cy)/(bx-cx)
            yint_cb = cy - slope_cb*cx
            xint_cb = -1*yint_cb*(1/slope_cb)
        # now search to see if either intercept is on the line segement
        if xint_cb == 'dne':
            pass
        elif (cx <= xint_cb <= bx) or (bx <= xint_cb <= cx):
            intercepts.append([xint_cb,'x'])
        if yint_cb == 'dne':
            pass
        elif (cy <= yint_cb <= by) or (by <= yint_cb <= cy):
            intercepts.append([yint_cb,'y'])
    


    # finally, check if 2 x-intercepts are opposite signs and 2 y-intercepts 
    # are opposite signs. If they are, the triangle contains the origin.
    px = nx = py = ny = 0
    for j in range(len(intercepts)):
        if intercepts[j][0] > 0 and intercepts[j][1] == 'x':
            px += 1
        elif intercepts[j][0] > 0 and intercepts[j][1] == 'y':
            py += 1
        elif intercepts[j][0] < 0  and intercepts[j][1] == 'x':
            nx += 1
        elif intercepts[j][0] < 0  and intercepts[j][1] == 'y':
            ny += 1
            
    if px >= 1 and py >= 1 and nx >= 1 and ny >= 1:
        count += 1
    # note that we need >= and not just ==. This is because if a vertice is
    # an intercept, then it will be duplicated because it is shared by two 
    # line segements, so we may in fact have more than 4 in the list.
        
print(count)
end = timeit.default_timer()

print()
print('runtime: ',end-start,'seconds')