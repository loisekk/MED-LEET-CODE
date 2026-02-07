class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        temp = ListNode(0)
        temp.next = head

        first = second = temp

        for _ in range(n):
            first = first.next

        while first.next:
            first = first.next
            second = second.next

        second.next = second.next.next

        return temp.next 
