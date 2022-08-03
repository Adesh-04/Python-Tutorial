## Add int if not found in list at probable place
# [1,2,4,5] int=3 ==> [1,2,3,4,5]

class Solution:
    def searchInsert(self, nums,target):
        self.nums = nums
        start = 0
        end = len(self.nums)

        while start < end:
            mid = start + (end - start) / 2
            mid = int(mid)
            print(mid)
            # print(mid)
            if self.nums[mid] == target:
                return mid
            elif target < self.nums[mid] :
                if target < self.nums[0]:
                    self.nums.insert(0,target)
                    return self.nums.index(target)
                elif end == mid :
                    if self.nums[end] > self.nums[end+1] :
                        self.nums.insert(end+1,target)
                        return end+1
                end = mid
            elif target > self.nums[mid] :
                if target > self.nums[-1]:
                    self.nums.append(target)
                    return self.nums.index(target)
                elif start == mid :
                    if self.nums[start] < self.nums[start+1]:
                        self.nums.insert(start+1,target) 
                        return start+1
                start = mid
        return -1


num = Solution()
val = num.searchInsert([0,1,410,511], -1)
# print(num.nums)
print(val)


        