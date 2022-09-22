from array import *
from operator import index
a=array('i',[])

n=int(input("Enter the length of the array: "))
for i in range(n):
    m=int(input(f"enter elemenet {i+1} of the array :"))
    a.append(m)
b=array('i',[])
for i in range(n):
    p=min(a)
    b.append(p)
    a.pop(a.index(p))#finding index of min element and removinf from a then again finding min element
print(b)