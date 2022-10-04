# Functions 
# there are two types of functions ---1st one is user defined  ---and 2nd is built in 
a=9
b=8
c=sum((a,b)) #sum is built in function 
print(c)

#user defined functions
def hello():
    print("hello")

hello()# so it will print whatever in the function 
print(hello) # here there is nothing ehich tjis function returns, but if we print any function it will print whatever function returns

#example

def fact(a):
    c=1
    for i in range(a):
        c=(i+1)*c
    return c

print(fact(5))

l=[1,2,3,"hi",0]
print(any(l)) # any is also one built in function

# The first line written in the function as what is this functinon for is known as docstring
def average(a,b):
    '''Hello this is a function for finding the average of two numbers'''
    return a+b/2

print(average.__doc__) # printing the docstring its very imp when the code has many function and you don't 
#know what it is doing