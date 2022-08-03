arr = [0,1,3]
print('normal list',arr)

print('\nmatrix')
matrix = [[0,1],[2,3],[4,5],[6,7]]
for i in matrix: print(matrix[matrix.index(i)])

print('\nassociative list i.e. dictionary')
assoc_arr = {0: [0,0], 1: [1,1]}
for i in assoc_arr: print(f'{i} ==> { assoc_arr.get(i)}')


list1 = [1,2,3,4]
del list1[2];  list1.remove(1)
print(list1)