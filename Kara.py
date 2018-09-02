import math
#def Kara(x,y):
    #x=int(input())
    #y=int(input()) #adjust the type
x=3141592653589793238462643383279502884197169399375105820974944592
y=2718281828459045235360287471352662497757247093699959574966967627
print(type(x))
l1=len(str(x))/2
print(l1)
a=int(x/(pow(10,l1)))#get a
print(x/(pow(10,l1)))
print(a)
b=x%(pow(10,l1))#get b
print(b)
c=int(y/(pow(10,l1)))#get c
d=x%(c*pow(10,l1))#get d
e=a*c
f=b*d
g=(a+b)*(c+d)-e-f

    #return Kara = Kara1*10^(len(x))+Kara3*10^(len*(x)/2)+Kara2

#print(Kara(x,y))
#print(e*pow(10,2*l1)+g*pow(10,l1)+f)