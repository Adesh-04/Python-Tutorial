x=int(input("1st Number :"))
y=int(input("2nd Number :"))
sum=x+y
print (sum) 

i=0
list1=[]
to_str = str(x)
leng = len(to_str)
for i in range (leng) :
    i=i+1
    b=x%10
    c=x-b
    x=c/10
    int_val = int(b)
    list1.append(int_val)
    if c==0:
        continue;
    if i==0:
        break;
print("\t", end=" ")
for ele in list1:
    print(ele,sep=" " , end=" ")
print()

print("+")


q=0
list2=[]
to_str = str(y)
leng = len(to_str)
for q in range (leng) :
    q+=1
    b1=y%10
    c1=y-b1
    y=c1/10
    int_val2 = int(b1)
    list2.append(int_val2)
    if c1==0:
        continue;
    if q==0:
        break;
print("\t", end=" ")
for ele in list2:
    print(ele,sep=" " , end=" ")
print( )

print("_"*25)


w=0
list3=[]
to_str = str(sum)
leng = len(to_str)
for w in range (leng) :
    w+=1
    b3=sum%10
    a3=sum-b3
    sum=a3/10
    int_val3 = int(b3)
    list3.append(int_val3)
    if a3==0:
        continue;
    if w==0:
        break;
print("\t", end=" ")
for ele in list3:
    print(ele,sep=" " , end=" ")
print()