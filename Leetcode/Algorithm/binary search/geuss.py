class Solution():
    def __init__(self,guess):
        self.guess1 = guess

    def guess(self,n):
        if self.guess1 > n:
            return 1
        elif self.guess1 < n:
            return -1
        else:
            return 0
    def guessNumber(self, n: int) -> int:
        start = 0
        end = n
        while start < end:
            mid = start + (end-start)/2
            num = self.guess(mid)
            # print(num)
            if num < 0:
                end = mid
            elif num == 1:
                start = mid
            else:
                return int(mid)
        return int(mid)

val = Solution(7518723913)
b = val.guessNumber(108738917310)
print(b)