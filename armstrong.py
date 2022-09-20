a= int(input("enter a number : "))
k=a
j=0
while(a>0):
    j=j+(a%10)**3
    a=a//10
if(k==j):
    print("It is an armstrong number")
else:
    print("Not an armstrong number")