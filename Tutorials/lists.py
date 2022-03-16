l1=[1,8,0,8,7]
for a in l1:
    for b in l1:
        for c in l1:
            for d in l1:
                if a>b>c>d:
                    print(a)
                    break

l12=[1,6,5] #unpacking
x,y,z=l12
print(y)
l2=[1,6,9,43]
mx=l2[0]
for i in l2:
    if i > mx:
        mx = i
print(mx)

matrix=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]
print (matrix[0][1])

l1.append(12)
print (l1)
l1.insert(1,2)
print(l1)
l1.remove(1)
print(l1)
l1.pop()
print(l1)
l1.index(8)
print(l1)
print(5 in l1)
print(l1.count(8))
l1.sort()
print(l1)
l1.reverse()
print(l1)

l9=[1,2,3,1,3,2,1]
l9.sort()
for i in l9:
    for j in l9:
        if i==j:
            l9.remove(j)
print (l9)

l8=[]
for i in l9:
    if i not in l8:
        l8.append(i)
print(l8)


