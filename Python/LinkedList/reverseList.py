# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prevNode = None
        currNode = head

        while currNode:
            nextNode = currNode.next  # 次のノードを保存 → 
            currNode.next = prevNode  # 現在のノードの次を前のノードに変更 ←
            prevNode = currNode  # 前のノードを現在のノードに更新 →
            currNode = nextNode  # 現在のノードを次のノードに更新 → 

        return prevNode

        # Time: O(n)
        # Space: O(1)