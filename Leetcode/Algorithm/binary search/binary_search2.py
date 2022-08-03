class Solution:
    def search(self, nums, target):
        self.nums = nums
        
        start = 0
        end = len(self.nums)
        
        if target in self.nums:
            while start < end:
                mid = start + (end - start) / 2
                mid = int(mid)
                if target == self.nums[mid]:
                    return mid
                elif target > self.nums[mid]:
                    start = mid
                elif target < self.nums[mid]:
                    end = mid
        else:
            return -1
        
            
            
    
        

val = Solution()
new = val.search([2,5],2)
print(new)
