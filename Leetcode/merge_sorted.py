class Solution:
    def merge(self, nums1 ,m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        self.nums1 = nums1
        self.nums2 = nums2
        
        self.nums1[:] = self.nums1[:m]
        
        for i in range(0,n):
            self.nums1.append(self.nums2[i])
            
        self.nums1.sort()
        return self.nums1
        
arr = Solution()
val = arr.merge( [ 1,2,3,4,0,0,0 ], 4 , [6,7,2] ,3 )
print(val)