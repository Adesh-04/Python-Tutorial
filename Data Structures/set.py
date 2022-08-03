sets = set([1,3,2,12,3,1,3,0,1,123,11,33])
setA = set([1,2,3])
setB = set([2,3,4,5,6])


## insertion
sets.add(122)

## deletion
sets.discard(1) 
sets.remove(33)

## Union
setC = setA|setB
print(setC)

## Intersection
setD = setA&setB
print(setD)

## Diffrerence
setE = setA-setB
setF = setB-setA
print(setE)
print(setF)

## Subset <= and Superset >=
print(setA <= setC)
print(setF >= setD)

for d in sets:
    print(d,end=' ')
