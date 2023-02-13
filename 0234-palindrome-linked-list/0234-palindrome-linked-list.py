# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):

        list1 = []
        list2 = []
        current = head 
        while current:
            list1.append(current.val)
            list2.append(current.val)
            current = current.next
        
        list2.reverse()

        return list1 == list2