import math as m
x=1;
dx=1;
itr=0;
while dx>0.00001:
     f=0.5*(7+m.log(x,10));
     itr=itr+1;
     dx=f-x;
     x=x+dx;
print(itr,x,dx)
