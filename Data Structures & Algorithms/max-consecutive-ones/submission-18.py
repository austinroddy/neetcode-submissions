class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        hs = 0
        for n in nums:
            if n == 1:
                i = i + 1
            else:
                i = 0
            if i > hs:
                hs = i
        return hs
        