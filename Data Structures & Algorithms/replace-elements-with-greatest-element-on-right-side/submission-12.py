class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            best = -1

            for j in range(i + 1, len(arr)):
                if arr[j] > best:
                    best = arr[j]

            arr[i] = best

        return arr