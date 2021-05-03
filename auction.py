#import sympy
import random
import statistics
import math

#Algorithm 1
m = int(input("Enter no of model owners:"))
n = int(input("Enter no of users:"))
C = []
k = 0
for i in range(n):
    temp = []
    for j in range(m):
        num = int(input("Enter bid of model owner {} for user {}:".format(j+1,i+1)))
        k = max(k,num)
        temp.append(num)
    C.append(temp)

D =[]
for i in range(n):
    D.append(int(input("Enter Demand of User {}:".format(i+1))))

sorted(D)

rep = []
for k in range(m):
    rep.append(float(input("Enter Reputation of Model Owner {}:".format(k+1))))
# or randomise above

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
            Priority[i+1].append(C[i][j]*rep[j])
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
    prior = []
    for j in T:
        prior.append(Priority[i-1][j-1])
    def delta(x):
        t = prior[T.index(x)]
        return t
    if (len(T) == 1):
        X[i] = T[0]
        P[X[i]] += temp
    else:
        T = sorted(T,key=delta)
        bid = []
        for j in T:
            bid.append(C[i-1][j-1])
        ma = 0
        if(prior[0]!=prior[1]):
            X[i] = T[0]
        else:
            for j in range(len(T)-1):
                if(prior[j] == prior[j+1]):
                    ma = max(ma,bid[j])
                    ma = max(ma,bid[j+1])
                else:
                    break
                X[i] = T[bid.index(ma)]
        

O = {} #Owner Mapping
for i in X:
    O[X[i]] = i

