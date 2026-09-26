from math import cos , sin , pi , sqrt
def pathlength(x,y):
    global L
    L=0
    i=1
    for i in range(len(x)-1):
        L=L+sqrt((x[i]+x[i-1])**2+(y[i]+y[i-1])**2)
    return L;
N=50
i=1
j=1
x=[]
y=[]
for i in range(N):
    z=0.5*cos(2*pi*i/N)
    x.append(z)
    z=0
    z=0.5*sin(2*pi*i/N)
    y.append(z)
    z=0
i=1
L=pathlength(x,y)
print(L)