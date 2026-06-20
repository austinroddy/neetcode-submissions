class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            print(f"idx {i} is {nums[i]}")
            if nums[i] == val:
                nums[i] = 101
            else:
                k = k + 1 
                print(f"k is now {k}")

        nums.sort()
        print(nums)
        print(k)
        return k