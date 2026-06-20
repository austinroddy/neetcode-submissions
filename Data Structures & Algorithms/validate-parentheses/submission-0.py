class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        d = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for char in s:
            if char in d:
                if stack and stack[-1] == d[char]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)

        return True if not stack else False
        
