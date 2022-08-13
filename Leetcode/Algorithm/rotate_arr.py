
class Solution():
    def rotateArr(self,arr,k):
        self.arr = arr

        while k:
            val = self.arr.pop()
            self.arr.insert(0,val)
            k-=1
        return self.arr

    def splice(self,arr,k):
        self.nums = arr[:-k]
        self.num = arr[-k:]
        self.new = self.num + self.nums
        return self.new

        

list1 = Solution()
val = list1.splice([1,2,3,4,5,6,7],3)
print(val)
