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
        if  not head or not head.next:
            return False

        slow = head.next
        fast = head.next.next

        while slow != fast: # if see same pointor
            if slow == fast: # see same pointor
                return True
            else:
                slow = slow.next # 1 step
                fast = fast.next.next # 2 step

        return True 
        