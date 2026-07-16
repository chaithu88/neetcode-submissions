# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current=head
        count=0
        while current:
            count+=1
            current=current.next
        if n<0 or n>count:
            return head
        if n==count:
            return head.next    
        index=count-n
        curr=head
        prev=None
        for _ in range(index):
            prev=curr
            curr=curr.next
        prev.next=curr.next
        return head
