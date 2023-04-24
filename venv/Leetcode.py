# def longestCommonPrefix(strs: list[str]) -> str:
#     result = ""
#     strs = sorted(strs)
#     first = strs[0]
#     last = strs[-1]
#     for i in range(min(len(first), len(last))):
#         if first[i] != last[i]:
#             return result
#         result += first[i]
#     return result
#
#
# print(longestCommonPrefix(["flower","flow","flight"]))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def fromlist(cls, lst):
        dummy = cls()
        head = dummy
        for i in lst:
            dummy.val = i
            dummy.next = cls()
            dummy = dummy.next
        dummy.next = None
        return head

    def tolist(self):
        pass

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = temp = ListNode(0)
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
            temp.next = list2 or list1
        return dummy.next



s1 = Solution().mergeTwoLists(ListNode.fromlist([1,2,4]), ListNode.fromlist([1,3,4]))
print(s1.tolist())
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]