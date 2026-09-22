class Solution:
    def isValid(self, s: str) -> bool:
        check = {")":"(","}":"{","]":"["}
        stack = []
        for i in s:
            if i in check:
                if not stack or stack[-1]!=check[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not stack
                