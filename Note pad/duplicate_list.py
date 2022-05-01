list =[1,3,6,1,4,6,6,1,5]

for item in list:
    item_count = list.count(item)
    if item_count == 1:
        # print(item)
        continue
    elif item_count > 1:
        
        list.remove(item)
        # print(list)
list.sort()
print(list)