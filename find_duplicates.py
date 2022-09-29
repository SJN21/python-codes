from itertools import count


l=["a","b",'c','f','k','a','c','k']
l2=[]
for i in l:
    if(l.count(i)>1):
        if(i not in l2):
            l2.append(i)
print(l2) #printing repeating terms

#printing unique elements
for i in l:
    if(i not in l2):
        print(i,end=" ")
for i in l2:
    print(i,end=" ")