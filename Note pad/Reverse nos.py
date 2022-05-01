x=int(input("Number="))
list1=[]
i=0
while x>0:
    a=x%10
    b=x-a
    x=b/10
    i+=1
    if a>0:
        list1.append(a)
    else :
        pass
#list1.reverse()
while i>0:
    a=list1[i-1]
    i-=1
    print (a)