class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0: return False 
        # Stack and mapping of brackets
        stack = []
        brackets = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in brackets:  # If it's an opening bracket
                stack.append(char)
            else:  # If it's a closing bracket
                if not stack or brackets[stack.pop()] != char:
                    return False

        # Check if all brackets are matched
        return not stack