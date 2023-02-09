import math
import random

import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
from matplotlib.pyplot import figure

n=51
s=(n,n)
a = np.zeros(s)
middle=(n//2,n//2)
plt.rcParams["figure.figsize"] = (15,15)
def distFromCentre(position,centre):
    return math.sqrt((position[0]-centre[0])**2+(position[1]-centre[1])**2)
for i in range(n):
    for j in range(n):
        a[i,j]=distFromCentre((i,j),middle)*2

def DrawBody(snake):
    for i in range(len(snake)-1):

        x1 = snake[i][0]
        y1 = snake[i][1]
        x2 = snake[i+1][0]
        y2 = snake[i+1][1]
        if (x1==x2):
            if(y1>y2):
                end=y1
                start=y2
            else:
                end = y2
                start = y1
            for j in range(start,end):
                a[x1][j]=0
        elif (y1==y2):
            if (x1 > x2):
                end = x1
                start = x2
            else:
                end = x2
                start = x1
            for j in range(start,end+1):
                a[j][y1]=0
def Danger(head):
    dangerweight=10
    for i in range(n):
        for j in range(n):
            if(((a[i][j]!=0) and (a[i][j]!=35)) and distFromCentre((i,j),head)<7):
                a[i, j] = a[i,j]+(100-distFromCentre((i, j), head)*dangerweight)
def Benefit(head):
    benefitweight=20
    for i in range(n):
        for j in range(n):
            if(((a[i][j]!=0) and (a[i][j]!=35)) and distFromCentre((i,j),head)<5):
                a[i, j] = a[i,j]-(100-(distFromCentre((i, j), head)*benefitweight))
snake1=[(20,1),(10,1),(10,20),(4,20),(4,30),(10,30),(10,22)]
snake2=[(n//2,n//2),(n//2,14),(12,14),(12,34)]
snake3=[(24,46),(40,46)]
apple=(20,20)
Benefit(apple)
DrawBody(snake1)
DrawBody(snake2)
DrawBody(snake3)
Danger((20,1))
Danger((24,46))
Danger((n//2,n//2))
a[24][46]=35
a[20][1]=35
a[20][20]=35
a[n//2][n//2]=35
for i in range (0):
    c=random.randint(0,n-1)
    b = random.randint(0, n-1)
    a[c][b]=35
    #Danger((c, b))
ax = sns.heatmap(a, linewidth=0)
plt.show()
