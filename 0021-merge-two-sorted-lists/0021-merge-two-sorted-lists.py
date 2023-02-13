# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):

      dummy = ListNode(None)
      current1 = list1 
      current2 = list2
      tail = dummy

      while current2 is not None and current1 is not None:
        if current2.val < current1.val:
          tail.next = current2
          current2 = current2.next 
        else:
          tail.next = current1
          current1 = current1.next 
        tail = tail.next

      if current1 is not None:
        tail.next = current1
      if current2 is not None:
        tail.next = current2

      return dummy.next