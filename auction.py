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
    D.append(int(input("Enter Demand of User {}:".format(i+1))))

sorted(D)
 
p = math.ceil((n+1)/2)
x = 0
V = {}
R = []
for i in range(m):
    V[i+1] = []
    temp = 0
    for j in range(n):
        if(C[i][j] > D[p-1] and D[j] <= D[p-1]):
            #V.append(i+1,j+1)
            V[i+1].append(j+1)
            temp = 1
            x = min(x,C[i][j])
        if(temp):
            R.append(j+1)
#print(V)
#print(R)
#print(x)
#Algorithm 2 
X = []
Y = R
P = {}#price by owner
Q = {}#payment of user
for i in Y:
    temp = x
    Q[i] = 0
    Q[i]+=temp
    T = 
