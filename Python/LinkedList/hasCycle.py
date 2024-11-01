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
        if not head or not head.next: # no data or only one node
            return False

        slow = head # init first pointer 
        fast = head.next # init next pointer

        while fast: # fast exist
            if slow == fast: # eventually see same pointer is cycle 
                return True
            slow = slow.next # 1 step 
            fast = fast.next.next # 2 step

        return False # no cycle 