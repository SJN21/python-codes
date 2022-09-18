a={"hi":"greeting", "g":"jhgjh", "d":{"a":"t","k":"i"}}
a["jh"]="ki"
print(a)
print(a["hi"])
print(a["d"])
print(a["d"]["a"])
print(a)
d3=a #to banne mathi delete thai gyu kemke equal aapyu che etle copy fun vapray
"""del d3["jh"]
print(d3)
print(a)
"""
#keys of a dictionary should be unique and immutable

#jo aapan ne na kbr hoy ke dictionary ma aa key che ke nai to e check karva aapde .get(key_we_want_to_check)
#even aa if else tarike pan kaam kari shake jo aapde lakhie d1.get('key',30) to jo aa key hase to eni value print
# karse pan nai hoy to 30 print karse
#we can't directly write print(dict1[key]) because if it is not it will give error and code will stop

d3=a.copy()
del d3["jh"]
print(d3)
print(a)