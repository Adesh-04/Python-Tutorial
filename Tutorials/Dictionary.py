customer ={
        "name":"John",
        "age":12,
        "is_verified":True
        }
customer["no"]=6574
print(customer.get("no"))

dict1={"1":"one","2":"Two","3":"Three"}
a=str(input('phone: '))
i=0
while i<3:
    b=""
    b=a[i]
    i+=1
    print(dict1[b])


dict={"1":"one","2":"two","3":"three"}
output=""
for i in a:
    output+= dict.get(i,"!")+" "
print (output)