import collections

dixt1 = {1: [0],2:[1]}
dixt2 = {4: [9],5:[10]}

res = collections.ChainMap(dixt1,dixt2)

print(res.maps)
print(list(res.keys()))
print(list(res.values()))

dixt1[2] = [2]   ## Automatic chainmap updation upon dict updation
print(res.maps)  