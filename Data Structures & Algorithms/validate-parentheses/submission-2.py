class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in pairs:
                if not check or check.pop() != pairs[i]:
                    return False
            else:
                check.append(i)
        return not check
            
        