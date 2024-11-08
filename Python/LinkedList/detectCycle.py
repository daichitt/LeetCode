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
        # No Cycle return None
        if not head or not head.next:
            return None
        
        slow = head # 1 step 
        fast = head # 1 step

        #
        while True:
            if not fast or not fast.next:
                # No Cycle return None
                return None

            fast = fast.next.next # 2 step
            slow = slow.next # 1 step

            if fast == slow: # if has Cycle
                break
        
        # init fast pointor
        fast = head

        # サイクル内で交差した地点から、両ポインタが同じノードに到達するまでには、必ずサイクルの開始点に向かうように進むためです。(同じ距離進む)
        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        return slow