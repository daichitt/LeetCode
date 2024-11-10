class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # use hash map (dict) # time O(n)
        stack = []

        brackets = {
            '(' : ')', 
            '{' : '}',
            '[' : ']', 
        }

        for braket in s:
            if braket in brackets.keys(): # key  such as '('
                stack.append(braket)
            elif braket in brackets.values():
                if not stack or brackets[stack.pop()] != braket:
                    return False
        
        return len(stack) == 0

        # check keys() and values()
