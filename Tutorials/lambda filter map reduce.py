from functools import reduce

listn = [1,2,3,4,1,5]

even = list(filter(lambda n : n%2 == 0, listn))

square = list(map(lambda n : n*n, listn))

multi = reduce(lambda a,b : a+b, listn)

print(even)
print(square)
print(multi)
