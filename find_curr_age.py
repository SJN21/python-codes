from datetime import *
now=datetime.now()
# print(now)
p=(input("Enter your birth date in the form od \"d-m-yy\""))
# to p to d-m-yy na form ma che ne aapde to je now che e ma seconds microsecond badhu che e form ma kai 
# rite onvertkarie to
then=datetime.strptime(p,'%d-%m-%y')
print(now-then)