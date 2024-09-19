class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        # Stack use LIFO
        for bracket in s:
            if bracket in pairs: # bracket is in key in pairs dict (open parentheses)
                stack.append(bracket) #
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:# check close bracket and poped 
                return False

        return len(stack) == 0
        