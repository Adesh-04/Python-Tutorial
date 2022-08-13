
class Solution():
    def twoSum(self,nums,target):
        self.nums = nums
        
        start,end = 0,len(self.nums)-1

        while start < end:
            res = self.nums[start] + self.nums[end]

            if res> target:
                end -=1
            elif res < target:
                start +=1
            elif res == target:
                return [start+1,end+1]

        





arr = Solution()
val = arr.twoSum( [-1,0],-1)
print(val)
