from typing import List

class Solution:
    def twoSum(self,nums: List[int], target : int) -> List[int]:
        nums.sort()
        current = 0
        for i in range(current,len(nums)):
            
            current+=1
            for j in range(current,len(nums)):
                
                if nums[i]+nums[j] == target:
                    print(nums)
                    return [i,j]
                elif nums[i]+nums[j] > target:
                    print(i,j , nums[i]+nums[j])
                    break
        

obj = Solution()
val = obj.twoSum([1,6,8,3,3,2],8)
print(val)