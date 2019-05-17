# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(0)
        cur = head
        while l1 is not None and l2 is not None:
            if l1.next is None and l2.next is not None:
                l1.next = ListNode(0)
            if l2.next is None and l1.next is not None:
                l2.next = ListNode(0)
            cur_val = (l1.val+l2.val+ carry)%10
            carry = int((l1.val+l2.val+carry)/10)
            if (l1.next is not None and l2.next is not None) or carry ==1:
                cur.next = ListNode(carry)
            cur.val = cur_val
            cur = cur.next
            
            l1=l1.next
            l2=l2.next
        return head