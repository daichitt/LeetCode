# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        curr = head

        while curr.next: 
            if curr.val == curr.next.val:
                curr.next = curr.next.next # 2 step (Slok deplicated Node)
            else:
                curr = curr.next # 1 step 
        
        return head