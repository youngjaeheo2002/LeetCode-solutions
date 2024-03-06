# Definition for singly-linked list.
#https://leetcode.com/problems/merge-k-sorted-lists/submissions/1195892263/
from ast import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def merge(self,left,right):
        print(f"merging {left} {right}")
        head = ListNode()
        current = head
        while(left or right):
            if left == None:
                current.next = right
                right = None

            elif right == None:
                current.next = left
                left = None

            else:
                if left.val < right.val:
                    current.next = ListNode(left.val)
                    left = left.next
                    current = current.next

                else:
                    current.next = ListNode(right.val)
                    right = right.next
                    current = current.next

        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        print(f"merging k lists {lists}")
        if lists == []:
            return None
        if len(lists) == 1:
            if lists[0] == []:
                return None
            return lists[0]
        mid = len(lists)//2

        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.merge(left,right)


if __name__ == "__main__":
    test1 = [
        ListNode(1,ListNode(4,ListNode(5))),
        ListNode(1,ListNode(3,ListNode(4))),
        ListNode(2,ListNode(6))
    ]

    solution = Solution()

    solution.mergeKLists(test1)
