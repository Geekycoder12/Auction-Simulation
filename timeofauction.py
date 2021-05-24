#import sympy
import random
import statistics
import math
import time
from typing import final
# from matplotlib import *
import matplotlib.pyplot as plt

import numpy as np
begin = time.time()
#Algorithm 1
# m = int(input("Enter no of model owners:"))
# n = int(input("Enter no of users:"))

mss = [25, 50, 75, 100]
nss = [100, 200, 300, 400]

final_result = []

for n in nss:
    for m in mss:
        D =[]
        for i in range(n):
            # D.append((int(input("Enter Demand of User {}:".format(i+1)))))
            D.append(random.randint(2,10))

        D.sort()
        #print(D)

        C = []
        k = 0
        for i in range(n):
            temp = []
            for j in range(m):
                # num = int(input("Enter bid of model owner {} for user {}:".format(j+1,i+1)))
                num = random.randint(0,10)
                k = max(k,num)
                temp.append(num)
            C.append(temp)

        Cost = {}
        for i in range(n):
            # Cost[i]=int(input("Enter Cost of user {}:".format(i)))
            Cost[i+1] = random.randint(1,D[i])

        Val = {}
        for i in range(m):
            # Val[i]=int(input("Enter Valuation of owner {}:".format(i)))
            Val[i+1] = random.randint(10,13)

        rep = []
        for k in range(m):
            # rep.append(float(input("Enter Reputation of Model Owner {}:".format(k+1))))
            rep.append(round(random.uniform(0,1), 2))
        # or randomise above

        p = math.ceil((n+1)/2)
        x = p
        # V = [[] for i in range(n)]
        V = {}
        Priority = {}
        R = []
        newuser = {}
        newowner ={}
        owneruser = {}
        for i in range(n):
            V[i+1] = []
            temp = 0
            Priority[i+1] = []
            for j in range(m):
                if(C[i][j] > D[p] and D[i] <= D[p ]):
                    #V.append(i+1,j+1)
                    V[i+1].append(j+1)
                    Priority[i+1].append(C[i][j]*rep[j])
                    # Priority[i+1][j+1] = C[i][j]*rep[j]
                    temp = 1
                    x = min(x,C[i][j])
            if(temp):
                    R.append(i+1)

        for i in range(n):
            bidmax = 0
            index = 0
            for j in range(m):
                if(bidmax< C[i][j]):
                    bidmax = C[i][j]
                    index = j
            newuser[i+1] = bidmax
            owneruser[i+1] = index+1
        userowner = {}
        for te in owneruser:
            userowner[owneruser[te]]= []
        for te in owneruser:
            userowner[owneruser[te]].append(te)




        for te in userowner:
            bidmin  = 99999999999
            k = 0
            if len(userowner[te]) >= 1:
                index = 0
                for j in userowner[te]:
                    # bidmin  = min(bidmin,C[j-1][te-1])
                    # print(te)
                    # print(j)
                    if(bidmin>C[j-1][te-1]):
                        bidmin = C[j-1][te-1]
                        k = j
            userowner[te] = k
            newowner[te] = bidmin
            

            
        hello = {}
        finalmap2 = {}
        for i in userowner:
            finalmap2[userowner[i]] = i
            hello[i] = C[userowner[i]-1][i-1]
        # print(finalmap2)

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
            for j in range(len(T)):
                prior.append(Priority[i][j])
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
                    P[X[i]] = min(C[i-1][T[0]-1],C[i-1][T[1]-1])
                else:
                    for j in range(len(T)-1):
                        if(prior[j] == prior[j+1]):
                            ma = max(ma,bid[j])
                            ma = max(ma,bid[j+1])
                        else:
                            break
                        X[i] = T[bid.index(ma)]
                        P[X[i]] = C[i-1][X[i]-1]
            #print(T)

        O = {} #Owner Mapping
        G = {} 
        for i in X:
            O[X[i]] = []
        for i in X:
            O[X[i]].append(i)
            G[X[i]] = C[i-1][X[i]-1]

        # Cost = {}
        # for i in X:
        #     # Cost[i]=int(input("Enter Cost of user {}:".format(i)))
        #     Cost[i] = random.randint(1,D[i-1])

        # Val = {}
        # for i in O:
        #     # Val[i]=int(input("Enter Valuation of owner {}:".format(i)))
        #     Val[i] = random.randint(10,13)

        #Algorithm 3
        Owner = {}
        userutil = {}
        ownerutil = {}
        for i in X:
            userutil[i] = Q[i] - Cost[i]
        totalindummy = 0
        for i in O:
                ownerutil[i] = Val[i] - P[i]
                totalindummy+=1

        newuserutil = {}
        newownerutil = {}
        for i in finalmap2:
            newuserutil[i] = newuser[i] - Cost[i]
        for i in userowner:
            newownerutil[i] = Val[i] - newowner[i]

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
        finalmap = {}
        total = 0
        for i in Owner:
            finalmap[Owner[i]] = i
            total+=1

        end = time.time()
        final_result.append(end-begin)

gr = [[final_result[j*len(nss)+i] for i in range(len(mss))] for j in range(len(nss))]

print(gr)

mar = ['o', '*', 's', '^']

for i in range(len(nss)):
    x_axis = [k for k in mss]
    y_axis = [gr[i][j] for j in range(len(nss))]
    ll = 'N = ' + str(nss[i])
    plt.plot(x_axis, y_axis, marker = mar[i], label = ll)
    plt.legend(prop = {'size':17}, loc = 'upper left')
    plt.xlabel("Number of model owners (M)", fontsize = 30)
    plt.ylabel("Time (in seconds)", fontsize = 30)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)

plt.show()

# fig = plt.subplots(figsize = (12, 8))

# fig = plt.subplots(figsize =(12, 8))
# x_axis  = [i for i in ownerutil]
# y_axis  = [ownerutil[i] for i in ownerutil]
# plt.bar(x_axis,y_axis)
# plt.xlabel('Model Owner',fontsize = 18)
# plt.ylabel('Utility',fontsize = 18)
# plt.xticks(fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.show() 
# fig = plt.subplots(figsize =(12, 8))
# x_axis = [i for i in finalmap]
# y_axis = [userutil[i] for i in finalmap]
# plt.bar(x_axis,y_axis)
# plt.xlabel('Data Owner',fontsize = 18)
# plt.ylabel('Utility',fontsize = 18)
# plt.xticks(fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.show()

# barwidth = 0.25
# fig = plt.subplots(figsize =(12, 8))
# bids = [G[i] for i in G]
# price = [P[i] for i in P]

# br1 = np.arange(len(bids))
# br2 = [i + barwidth for i in br1]
# # print(br1)
# # print(br2)
# plt.bar(br1,bids,color='r',width=barwidth,edgecolor='grey',label='Bid')
# plt.bar(br2,price,color='g',width=barwidth,edgecolor='grey',label='Price')

# plt.xlabel('Model Owner',fontsize=30)
# plt.ylabel('Bids and Prices',fontsize=30)
# plt.xticks([r + barwidth for r in range(len(bids))],[r for r in G],fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.legend(prop = {'size':20})
# plt.show()

# #Payments and Demands of users
# barwidth = 0.25
# fig = plt.subplots(figsize =(12, 8))
# dem = [D[i-1] for i in finalmap]
# payme = [Q[i] for i in finalmap]

# br1 = np.arange(len(dem))
# br2 = [i + barwidth for i in br1]

# plt.bar(br1,dem,color='r',width=barwidth,edgecolor='grey',label='Demands')
# plt.bar(br2,payme,color='g',width=barwidth,edgecolor='grey',label='Payments')

# plt.xlabel('Winning User',fontsize=30)
# plt.ylabel('Demands and Payments',fontsize=30)
# plt.xticks([r + barwidth for r in range(len(dem))],[r for r in finalmap],fontsize = 20)
# plt.yticks(fontsize = 20)

# plt.legend(prop = {'size':20})
# plt.show()
# fig = plt.subplots(figsize =(12, 8))
# x_axis  = [i for i in newownerutil]
# y_axis  = [newownerutil[i] for i in newownerutil]
# plt.bar(x_axis,y_axis)
# plt.xlabel('Model Owner',fontsize = 30)
# plt.ylabel('Utility',fontsize = 30)
# plt.xticks(fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.show() 
# fig = plt.subplots(figsize =(12, 8))
# x_axis  = [i for i in newuserutil]
# y_axis  = [newuserutil[i] for i in newuserutil]
# plt.bar(x_axis,y_axis)
# plt.xlabel('User',fontsize = 30)
# plt.ylabel('Utility',fontsize = 30)
# plt.xticks(fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.show() 

# barwidth = 0.25
# fig = plt.subplots(figsize =(12, 8))

# bids = [hello[i] for i in hello]
# price = [newowner[i] for i in newowner]

# br1 = np.arange(len(bids))
# br2 = [i + barwidth for i in br1]
# # print(br1)
# # print(br2)
# plt.bar(br1,bids,color='r',width=barwidth,edgecolor='grey',label='Bid')
# plt.bar(br2,price,color='g',width=barwidth,edgecolor='grey',label='Price')

# plt.xlabel('Model Owner',fontsize=30)
# plt.ylabel('Bids and Prices',fontsize=30)
# plt.xticks([r + barwidth for r in range(len(bids))],[r for r in hello],fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.legend(prop = {'size':20})
# plt.show()
# barwidth = 0.25
# fig = plt.subplots(figsize =(12, 8))
# dem = [D[i-1] for i in finalmap2]
# payme = [newuser[i] for i in finalmap2]

# br1 = np.arange(len(dem))
# br2 = [i + barwidth for i in br1]

# plt.bar(br1,dem,color='r',width=barwidth,edgecolor='grey',label='Demands')
# plt.bar(br2,payme,color='g',width=barwidth,edgecolor='grey',label='Payments')

# plt.xlabel('Winning User',fontsize=30)
# plt.ylabel('Demands and Payments',fontsize=30)
# plt.xticks([r + barwidth for r in range(len(dem))],[r for r in finalmap2],fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.legend(prop = {'size':20})
# plt.show()

