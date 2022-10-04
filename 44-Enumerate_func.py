#enumerate functions e code ne jaldi lakhva vapray che suppose
l1=["kakdi","tindola","bhinda","kankoda"]

#have aa list na badha sha nathi lava mummy khe che hu majak karti ti khali odd number par kidhela shaak lavje to

i=1
for item in l1:
    if(i%2!=0):
        print(f"buy {item}")
    i+=1

#aanej aam pan lakhay

for index, item in enumerate(l1):
    if(index%2==0):
        print(f"buy {item}")

#enumerate function index and item banne aape etle banne ek sathe vapri shakay alag thi i variable levani
# jaroor nai pade