n=int(input("enter the no of terms"));
a=1;
b=1;
i=1;
while  (i<= n) :
    if(i==1):
        print(a);
    elif(i==2):
        print(b);
    else:
        c=a+b;
        print(c);
        a=b;
        b=c;
    i+=1;

        