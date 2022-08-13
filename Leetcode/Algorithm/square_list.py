
class Solution():
    def sortedSquares(self,nums):
        self.nums = nums
        self.sorted = []

        for ele in nums:
            ele = ele ** 2
            self.sorted.append(ele)

        self.sorted.sort()
        
        return self.sorted

    def sortSq(self,nums):
        self.nums2 = nums
        self.sorted = []
        val = [ele**2 for ele in self.nums]
        val.sort()
        return val

        
sort = Solution()
val = sort.sortedSquares([1,2,6,3])
val2 = sort.sortSq([1,2,3,4])
print(val2)
    