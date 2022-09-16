# strings

var1= "Hi, this is SJN"
#here the string is saved in var1

print(var1)
#prints whole string

print(len(var1))
#tells the length
print(var1 [3])
#prints that element of string

print(var1[0:5])
#it will print first 5 characters starting from 0 to 4 it will exclude 5th

print(var1[:33])
print(var1[7:], end='\n')
print(var1[:6], end='\n')
print(var1[:])
print(var1[-7:-4])

#string slicing

print(var1[0::2])
print(var1[::])
print(var1[::-1])
print(var1[:6:-1])
print(var1[-6:-4])

a="""
h i
o o
 - """
 #for multi line string use 3' or 3"
print(a)

#formatted string - fstrings
a='jainam'
b=33
print(f"my name is {a} and age is {b}")
#same can be written as
print("my name is {} and age is {}".format(a,b))
# we can write by index as well
print("my name is {1} and age is {0}".format(a,b))

print(var1.count("a"))
a="      haafjgv"
print(a.strip())