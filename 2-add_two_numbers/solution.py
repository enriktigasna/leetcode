# Beats 100% Memory

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def list_to_LL(self, arr):
        if len(arr) < 1:
            return None

        if len(arr) == 1:
            return ListNode(arr[0])
        return ListNode(arr[0], next=self.list_to_LL(arr[1:]))
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        num1 = 0
        num2 = 0
        while l1:
            num1 += l1.val * 10**i
            i += 1
            l1 = l1.next
        i = 0
        while l2:
            num2 += l2.val * 10**i
            i += 1
            l2 = l2.next
        res = [int(x) for x in str(num1 + num2)]
        res.reverse()
        return self.list_to_LL(res)
        