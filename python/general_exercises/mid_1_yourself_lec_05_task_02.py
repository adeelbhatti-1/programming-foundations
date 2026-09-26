from math import exp,sin
#def y(x):
#    y=exp(x)
#    return y
def df(h,x,y):
    return (y[1]-y[0])/1.0*h
def dff(h,x,y):
    return (y[0]-2*y[1]+y[2])/h**2
def dfff(h,x,y):
    return (y[2]-y[0])/2.0*h
h=1
x=[0,1,2,3,4]
y=[exp(0),exp(1),exp(2),exp(3),exp(4)]
ds=[]
j=1
for j in range(len(x)-3):
    z=dfff(h,x[j:j+3],y[j:j+3])
    ds.append(z)
    print('dfff=[%d]=%.5f' %(x[j],z))
