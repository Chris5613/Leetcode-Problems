# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        current = head
        prev = None
        while current is not None:
            if current.val == val:
                if prev:
                    prev.next = current.next
                else:
                  head = current.next
                current = current.next
            else:
                prev = current
                current = current.next        
        return head