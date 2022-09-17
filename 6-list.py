grocery=["mug","dal","soap","sugar"]
numbers=[5,3,8,1,2]
#print(len(numbers))
numbers[1]=6
print(numbers)
print(grocery)
grocery.append("harpic")
print(grocery)
grocery.insert(3,"deodrant")
print(grocery)
grocery.extend("hi")
print(grocery)
grocery[1]="jks"

# jo aapde koi list joie che jema 1 to 100 hoy to for loop chalai append karvani jaroor nathi we can do like
l=[i for i in range(1,100)]
print(l)
# or 
l1=list(range(1,100))
print(l1)

grocery.remove("h")
print(grocery)
grocery.pop(3)
print(grocery)
grocery.pop()
print(grocery)

print(max(numbers))
print(min(numbers))
print(len(numbers))

a=grocery.count("mug")
print(a)

grocery.reverse()
print(grocery)
numbers.sort()
print(numbers)

# join operator - this is main for the strins see
s=" "
l=['hi','my','name','is','jainam']
s=s.join(l)#it will join s after each element of iterable here list
print(s)

#list unpacking
l2=[1,2,3,4,5,6,7,8,9]
# we can directly assign values like this a,b,c=1,2,3 but we can put it in list and other values as it is in list see
a,b,c,*other,d=[1,2,3,4,5,6,7,8,9]
#*other will tack every other remaining elements here * will tell to take all other values you can write *var_name 
# instead of *other other is just a name
print(a,b,c,other,d)

#we can unpack tuples as well in this way--only 2 methods-count and index

grocery.clear()
print(grocery)
print(type(grocery))
a=(1,4,3,2,2)
print(type(a))
a=list(a)
print(type(a))
a.insert(4,3)
print(a)
print(~10)
print(~12)
print(~11)
#slicing same as in string -- aa ek navi copy banavse list ni with the new changes pan list ma koi change nai thay
#jo list ma change karvu hoy to list_name=list[::-1]

#adding --- append,insert,extend(in this list will be the input)
#remove --- clear,remove,pop
#finding---finding position---index--like index('d') then returns the index
#                                        if we write index('d',0,4)then in list find d from 0th ele to 3rd ele only
#                             count--return how many times it occurs in the string

# sorting- list.sort()--method--it will not return a new list it will return none just modify last list and display
#          sorted(list)--built in function--creates new list with changes
