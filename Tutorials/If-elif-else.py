price=1000000
is_credit_good=False
if is_credit_good:
    print ("put down 10%")
    print (price/10 ,"$")
else :
    print ("put down 20%")
    print (price/5 ,"$")
    
has_high_income=True
has_good_credit=False
if has_high_income and has_good_credit:
    print('Eligible for the loan')
if has_high_income or has_good_credit:
    print('Eligible for loan')

temp=24
if temp>30:
    print ("It's a hot day")
elif temp<12:
    print ("It's a cold day")
else:
    print ("It's neither cold nor hot")
    
name="adesh"
x=len(name)
if x<=3:
    print("name must have 3 characters")
elif x>=50:
    print("name must have less than 50 characters")
else:
    print("name looks good")

a=int(input("Weight:"))
b=input("(l)bs or (k)ilo :")
c=b.lower()
if c=="l":
    print (a*0.45)
elif c=="k":
    print (a/0.45)
else:
    print('Invalid command')