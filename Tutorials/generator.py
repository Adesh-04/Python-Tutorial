# generators are best when dealing with millions of data values
# it does not store *any* values in memory making it faster than conventional method

def square(list):
    for element in list:
        yield element * element   # yield makes it generator

insert = square([5,4,1,55,1])

print(insert)

for num in insert:
    print (num)

# print(next(insert)) 


# nums = (x*x for x in [1,4,2,6,1,5])   # generator comprehension use [] for list comprehension
# print(nums)

# print( list(nums))   # using list it will store all the records of data

# for num in nums:
    # print (num)      