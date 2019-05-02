# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:42:18 2019

@author: aguec
"""

def pascal_middle(n):
    
#                         1
#                        1 1
#                       1 2 1
#                      1 3 3 1
#                     1 4 6 4 1
#                    1 5 10 10 5 1
#                   1 6 15 20 15 6 1
                   
#              1----1---1---1---1---1
#              |   |   |   |   |   |   we can see the relationship b/w pascal's
#              1---2---3---4---5---6- triangle and the grid movements
#              |   |   |   |   |   |
#              1---3---6---10-------  every corner is the middle entry in the
#              |   |   |   |   |   |  2^n row of the triangle
#              1---4---10--20-------
#              |   |   |   |   |   | thus if we can write a program for the 
#              1-------------------- triangle, we access that value for the
#              |   |   |   |   |   | nxn grid to see how many ways we can 
#              1--------------------- complete it.
    
    pascal = [[1],[1,1]]
    for i in range(2,n):
        row =[1]
        for j in range(i-1):
            row.append(pascal[i-1][j]+pascal[i-1][j+1])
        row.append(1)
        pascal.append(row)

    #  for an nxn grid, we want the mimddle entry of the 2*n row
    # the middle entry is the n/2 position in that row
    # set n >= 41 to get the correct result for the 20x20 grid:
    
    print(pascal[40][20])