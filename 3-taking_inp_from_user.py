#Taking variables from users

# Way 1
    # IMP->Whenever we tack input it will be stored as an string so we can not add int directly
print("enter a num")
a=input()
    # print(a+3)  -> it will throw error bcz a is string and 3 is int so correct code is
print(int(a)+3)

# way 2
a=int(input("enter a num\n")) #->directly casted into int
print(a+3)

#way 3
a=input("enter a no.\n") #->here it will print the line as well take input and store it in variable
print(int(a)+3)