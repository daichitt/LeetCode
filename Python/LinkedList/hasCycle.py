# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: ## it can be null 
            return False

        slow = head.next # 1 step 
        fast = head.next.next # 2 step

        while slow != fast: # eventually see same ppointer if hasCycle
            if not slow or not slow.next: # not hasCycle
                return False

            slow = slow.next # 1 step 
            fast = fast.next.next # 2 step

        return True