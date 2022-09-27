from multiprocessing.sharedctypes import Value
from re import L


dict={"article":"a particular item or object", "disease":"a particular quality or disposition regarded as adversely affecting a person or group of people.", "prime number":"a number that is divisible only by itself and 1 "}
print("find any values from")
for a, b in dict.items():
    print(a)
a=input()
print(dict[a])
for a, b in dict.items():
    print(b)

#have list ma
l=['c','d','e',33]
for i in l:
    print(i)