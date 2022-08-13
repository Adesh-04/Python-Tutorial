
class Solution():
    def moveZero(self,nums):
        self.nums = nums
        [ self.nums.remove(x) or self.nums.append(x) for x in self.nums if x == 0 ]
        

        return self.nums


arr = Solution()
val = arr.moveZero([ 1,2,3,0,7,11 ])

print(val)