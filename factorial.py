n=int(input("Enter a number : "))

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=(i)*fact
    return fact
print(factorial(n))
a=input("Enter name: ")
l=a.split()
print(l[0],l[2])
a=True
print(type(a))