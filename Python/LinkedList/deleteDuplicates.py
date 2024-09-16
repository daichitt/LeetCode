# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head #points to front of linked list

        while current.next: # until next exist 
            if current.val == current.next.val:
                current.next = current.next.next # set next = next.next (skip)
            else:  # not deplicate
                current = current.next

        return head

        
        