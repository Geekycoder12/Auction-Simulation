#import sympy
import random
import statistics
import math
import matplotlib.pyplot as plt
import numpy as np

#Algorithm 1
m = int(input("Enter no of model owners:"))
n = int(input("Enter no of users:"))

D =[]
for i in range(n):
    D.append((int(input("Enter Demand of User {}:".format(i+1)))))

D.sort()
print(D)

C = []
k = 0
for i in range(n):
    temp = []
    for j in range(m):
        num = int(input("Enter bid of model owner {} for user {}:".format(j+1,i+1)))
        k = max(k,num)
        temp.append(num)
    C.append(temp)



rep = []
for k in range(m):
    rep.append(float(input("Enter Reputation of Model Owner {}:".format(k+1))))
# or randomise above

p = math.ceil((n+1)/2)
x = p
V = [[] for i in range(n)]
Priority = {}
R = []
for i in range(n):
    temp = 0
    Priority[i] = []
    for j in range(m):
        if(C[i][j] > D[p-1] and D[i] <= D[p-1]):
            #V.append(i+1,j+1)
            V[i].append(j)
            Priority[i].append(C[i][j]*rep[j])
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
    T = V[i-1]
    prior = []
    for j in T:
        prior.append(Priority[i-1][j-1])
    def delta(x):
        t = prior[T.index(x)]
        return t
    if (len(T) == 1):
        X[i] = T[0]
        P[X[i]] = temp
    else:
        T = sorted(T, key=delta)
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
        
print(T)

O = {} #Owner Mapping
G = {} 
for i in X:
    O[X[i]] = []
for i in X:
    O[X[i]].append(i)
    G[X[i]] = C[i-1][X[i]-1]

Cost = {}
for i in X:
    Cost[i]=int(input("Enter Cost of user {}:".format(i)))

Val = {}
for i in O:
    Val[i]=int(input("Enter Valuation of owner {}:".format(i)))

#Algorithm 3
Owner = {}
userutil = {}
ownerutil = {}
for i in X:
    userutil[i] = Q[i] - Cost[i]

for i in O:
    try:
        ownerutil[i] = Val[i] - P[i]
    except:
        ownerutil[i] = 0

for i in O:
    Z = O[i]
    tempownerutil = []
    for j in Z:
        x = (C[j-1][i-1] - P[i])
        tempownerutil.append(x)
    def utility(x):
        t = tempownerutil[Z.index(x)]
        return t
    tempownerutil.sort(reverse=True)
    Z = sorted(Z,key=utility)
    if len(Z)==1:
        Owner[i] = Z[0]
    else:
        if(tempownerutil[0]!=tempownerutil[1]):
            Owner[i] = Z[0]
        else:
            l=0
            b=0
            for j in range(len(Z)-1):
                if (tempownerutil[j]==[j+1]):
                    b = j+1
                else:
                    break
            l = random.randint(0,b)
            Owner[i] = Z[b]

print(P)
print(Q)
print(G)
print(userutil)
print(ownerutil)


# x_axis = [i for i in ownerutil]
# y_axis = [ownerutil[i] for i in ownerutil]

# plt.plot(x_axis, y_axis)
# plt.title('Utility of Owers')
# plt.xlabel('Model Owner')
# plt.ylabel('Utility of Model Owners')
# plt.show()

x_axis  = [i for i in ownerutil]
y_axis  = [ownerutil[i] for i in ownerutil]
plt.bar(x_axis,y_axis)
plt.show() 

x_axis = [i for i in userutil]
y_axis = [userutil[i] for i in userutil]
plt.bar(x_axis,y_axis)
plt.show()

barwidth = 0.25
fig = plt.subplots(figsize =(12, 8))
bids = [G[i] for i in G]
price = [P[i] for i in P]

br1 = np.arange(len(bids))
br2 = [i + barwidth for i in bids]

plt.bar(br1,bids,color='r',width=barwidth,edgecolor='grey',label='Bid')
plt.bar(br2,price,color='g',width=barwidth,edgecolor='grey',label='Price')

plt.xlabel('Model Owner',frontweight='bold',fontsize=15)
plt.ylabel('Bids and Payments',frontweight='bold',fontsize=15)
plt.xticks([r + barwidth for r in range(len(bids))],[r for r in G])

plt.legend()
plt.show()

