#import sympy
import random
import statistics
import math

#Algorithm 1
m = int(input("Enter no of model owners:"))
n = int(input("Enter no of users:"))
C = []
p = 0
for i in range(n):
    temp = []
    for j in range(m):
        num = int(input("Enter bid of model owner {} for user {}:".format(j+1,i+1)))
        p = max(p,num)
        temp.append(num)
    C.append(temp)

D =[]
for i in range(n):
    D.append(int(input("Enter Demand of User {}:".format(i+1))))

sorted(D)
 
p = math.ceil((n+1)/2)
x = p
V = {}
Priority = {}
R = []
for i in range(n):
    V[i+1] = []
    Priority[i+1] = []
    temp = 0
    for j in range(m):
        if(C[i][j] > D[p-1] and D[i] <= D[p-1]):
            #V.append(i+1,j+1)
            V[i+1].append(j+1)
            Priority[i+1].append(C[i][j]*R[j])
            temp = 1
            x = min(x,C[i][j])
        if(temp):
            R.append(i+1)
#print(V)
#print(R)
#print(x)
#Algorithm 2 
X = {}
Y = R
P = {}#price by owner
Q = {}#payment of user

for i in Y:
    temp = x
    Q[i] = 0
    Q[i]+=temp
    T = V[i]
    def delta():
        return Priority[i][]
    if (len(T) == 1):
        X[i] = T[0]
        P[X[i]] += temp
    else:
        sorted(T,key=delta)