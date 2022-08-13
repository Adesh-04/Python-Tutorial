## not Completed
class Solution():
    def sum_subarray(self,nums):
        self.nums = nums
        arr1 = []     
        arr2 = []
        total = sum(self.nums)
        total_x = 0

        for i in range(0,len(self.nums)):
            arr1[:] = self.nums[i:4+i]
            total_y = sum(arr1)
            if len(arr1) < 4:
                break
            elif total_y > total and total_y > total_x:
                total_x = total_y
                arr2[:] = arr1[:]
            if total < total_x:
                return total_x
        return arr2,total
        




arr = Solution()
val = arr.sum_subarray( [5,4,-1,7,8,1] )
print(val)

