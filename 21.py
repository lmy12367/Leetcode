from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1=list1
        h2=list2
        temp1=ListNode(0)
        temp2=ListNode(0)
        while(h1.next!=None|h1.next!=None):
            temp1.next=h1.next
            temp2.next=h2.next
            if list1.val<list2.val:
                list1.next=list2
                list2.next=temp1.next
            else:
                list2.next=list1
                list1.next=temp2.next

            h1=temp1.next
            h2=temp2.next

        return list1

sol=Solution()
s1=sol.mergeTwoLists([1,2,4],[1,3,4])
print(s1)