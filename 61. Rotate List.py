# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        length = 1
        rot = head
        while rot.next:
            rot = rot.next
            length +=1
        
        k =  k % length
        if k == 0:
            return head
        rot.next = head
        steps = length - k 
        new_rot = head
        for _ in range(steps - 1):
            new_rot = new_rot.next
        new_head = new_rot.next
        new_rot.next = None

        return new_head
        