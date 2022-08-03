class Solution:
    def search(self, nums, target):
        self.nums = nums
        
        start = 0
        end = len(self.nums)
        mid = self.findMid(start,end)
        
        if target in self.nums:
            if end == 1:
                return start
            while True:
                if target == self.nums[mid]:
                    return mid
                elif target < self.nums[mid]:
                    if end == mid:
                        mid -= 1
                    end = mid
                    mid = self.findMid(start,end)
                
                elif target > self.nums[mid]:
                    if start == mid:
                        mid += 1
                    if start == end:
                        return -1
                    start = mid
                    mid = self.findMid(start,end)
        else:
            return -1
            
            
    def findMid(self,start,end):
        mid = start + end
        mid = mid // 2
        return mid
        

val = Solution()
new = val.search([2,5],0)
print(new)
