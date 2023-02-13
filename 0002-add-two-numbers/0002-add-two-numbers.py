# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(None)
        tail = dummy
        current1 = l1 
        current2 = l2 
        carry = 0

        while current1 or current2 or carry == 1:
            val1 = 0 if current1 is None else current1.val 
            val2 = 0 if current2 is None else current2.val

            sum = val1 + val2 + carry 
            carry = 1 if sum > 9 else 0
            digit = sum % 10

            tail.next = ListNode(digit)
            tail = tail.next 

            if current1 is not None:
                current1 = current1.next 
            if current2 is not None:
                current2 = current2.next 
        return dummy.next
