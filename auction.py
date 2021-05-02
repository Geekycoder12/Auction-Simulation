#import sympy
import random
import statistics
import math

#Algorithm 1
m = int(input("Enter no of model owners:"))
n = int(input("Enter no of users:"))
C = []
for i in range(m):
    temp = []
    for j in range(n):
        temp.append(int(input("Enter bid of model owner {} for user {}:".format(i+1,j+1))))
    C.append(temp)

D =[]
for i in range(n):
    D.append(int(input("Enter Demand of User {}".format(i+1))))

sorted(D)
 
p = math.ceil((n+1)/2)
x = 0
V = []
R = []
for i in range(m):
    for j in range(n):
        if(C[i][j] > D[p] and D[j] < D[p]):
            V.append(i,j)
            R.append(i)
            x = min(x,C[i][j])

