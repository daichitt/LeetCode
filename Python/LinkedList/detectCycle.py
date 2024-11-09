# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: 
            return None

        slow = head # start with 0nd Node
        fast = head.next # start with 1nd Node 

        while True:
            if slow.val == fast.val: # see same pointor
                break
            else:
                slow = slow.next # 1 step
                fast = fast.next.next # 2 step

        # init fast pointor
        fast = head  # bask to 0nd Node

        while fast != slow: # not see the same pointor
            slow = slow.next # 1 step
            fast = fast.next.next # 2 step
        return slow