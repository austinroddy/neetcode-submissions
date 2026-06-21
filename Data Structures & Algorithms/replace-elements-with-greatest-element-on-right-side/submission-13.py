class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        best = -1

        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = best
            best = max(best, current)

        return arr