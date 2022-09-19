#aapde already arguments,parameters vaccheno difference joyo and also aapde argument ma keyword aargument,default 
# parameters and positional aarguments pan aapdi pase emna mate special char pan che like
#*args  and   **kwargs
def super_func(*args):
    return sum(args)
print(super_func(1,2,3,4,5))
#*args means tame game tetli values ne as an argument aapi shako e badhi lese and then badhano sum kari ne 
# return karse
# args khali variable name che eni jagyae koi pan naam apay pan standard args che


#similarly for kwargs we can add any number of keyword arguments after aargs like this see
def super_func(*args,**kwargs):
    print(kwargs)
    s=0
    for i in kwargs.values():
        s+=i
    return sum(args)+s
print(super_func(1,2,3,4,5, n1=5,n2=8,n3=9))
