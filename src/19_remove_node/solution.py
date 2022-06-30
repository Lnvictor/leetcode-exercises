# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = head
        count = 0

        if curr.next is None:
            if n == 1:
                return None
            return head

        while curr is not None:
            count += 1
            curr = curr.next

        curr = head
        if count - n == 0:
            return head.next

        for i in range(count - n - 1):
            curr = curr.next

        curr.next = curr.next.next
        return head
