# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNumber(l:Optional[ListNode])->int:
            if not l:
                return 0
            return l.val + 10*getNumber(l.next)
        sum = getNumber(l1) + getNumber(l2)
        print(sum)
        dummy = ListNode(0)
        returnVal = ListNode(0,dummy)
        
        if sum == 0:
           return dummy

        while(sum>0):
            num = sum %10
            dummy.val = num
            sum = sum//10
            if(sum > 0):
                dummy.next = ListNode()
            dummy = dummy.next

            

        return returnVal.next
