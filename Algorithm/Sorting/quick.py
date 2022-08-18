# Time Complexity = O(n**2) Omega(n * log(n)) 
# Space Complexity = O(1)

arr = []

with open('1000.txt','r') as f:
    val = f.read()
arr = val.split(',')
arr.pop()

def partition(l, r, nums):
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if int(nums[i]) <= int(pivot):
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr
 

 
def quickSort(l, r, nums):
    if len(nums) == 1:  
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quickSort(l, pi-1, nums) 
        quickSort(pi+1, r, nums) 
    return nums




quickSort(0,len(arr)-1,arr)
print(arr)
