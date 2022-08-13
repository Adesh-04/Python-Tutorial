import math
class Solution():
    def pivotIndex(self,nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1



obj = Solution()
val = obj.pivotIndex( [-1,-1,-1,-1,-1,0] )
print(val)