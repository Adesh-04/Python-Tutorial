
class Solution():
    def twoSum(self,nums,target):
        self.nums = nums
        self.nums.sort()
        step = 1

        for i in range(0,len(self.nums)):
            step = 1
            if self.nums[i] <= target:
                for j in range(step,len(self.nums)):
                    if self.nums[i]+ self.nums[i+1] == target:
                        return [i+1,i+2]
                    if self.nums[i] + self.nums[j] == target:
                        return [i+1,j+1]
                    if self.nums[j] > ((target)**2)**0.5  :
                        break
                    else: 
                        step += 1
            if self.nums[i] > target:
                break
        return None

arr = Solution()
val = arr.twoSum( [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],5)
print(val)

