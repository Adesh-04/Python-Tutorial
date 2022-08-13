
class Solution():
    def contains_duplicate(self,nums):
        self.nums = nums
        sets = set(self.nums)

        if len(sets) < len(self.nums):
            print(True)
        else:
            print(False)

arr = Solution()
arr.contains_duplicate( [0,1,2,2,3] )