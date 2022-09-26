#faults 5*7=33,6/2=2,9+11=18,17-32=15
a=int(input("Enter first num: "))
b=int(input("Enter second num: "))
c=input("Enter operand: ")
if(c=="+"):
    if(a==9 and b==11):
        print(18)
    else:
        print(a+b)
if(c=="*"):
    if(a==5 and b==7):
        print(33)
    else:
        print(a*b)
if(c=="-"):
    if(a==17 and b==32):
        print(15)
    else:
        print(a-b)
if(c=="/"):
    if(a==6 and b==2):
        print(2)
    else:
        print(a/b)