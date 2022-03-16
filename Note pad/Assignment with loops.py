x=int(input("1st Number :"))
y=int(input("2nd Number :"))
sum=x+y
print sum :

i=0:
list1=[]
for i in range (5) :
    i=i+1
    b=x%10
    c=x-b
    x=c/10
    list1.append(b)
    if c==0:
        continue;
    if i==0:
        break;
print  " " ,list1[4],list1[3],list1[2],list1[1],list1[0]

print("+")


q=0
list2=[]
for q in range (5) :
    q+=1
    b1=y%10
    c1=y-b1
    y=c1/10
    list2.append(b1)
    if c1==0:
        continue;
    if q==0:
        break;
print  " " ,list2[4],list2[3],list2[2],list2[1],list2[0]

print("_"*15)


w=0
list3=[]
for w in range (5) :
    w+=1
    b3=sum%10
    a3=sum-b3
    sum=a3/10
    list3.append(b3)
    if a3==0:
        continue;
    if w==0:
        break;
print  " " ,list3[4],list3[3],list3[2],list3[1],list3[0]
