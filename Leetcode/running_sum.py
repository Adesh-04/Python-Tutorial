
class Solution():
    def run_sum(self,nums):
        self.nums = nums
        arr = []

        for index,i in enumerate(self.nums):
            if index == 0:
                arr.append(self.nums[0])
            else:
                val = arr[index-1] + i
                arr.append(val)
        print(arr)

obj = Solution()
obj.run_sum( [1,2,3,4] )