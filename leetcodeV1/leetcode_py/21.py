from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        current=dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            
            current=current.next
        
        current.next= list1 if list1 else list2

        return dummy.next
    
def build_linked_list(lst):
    dummy=ListNode(0)
    current=dummy
    for val in lst:
        current.next=ListNode(val)
        current=current.next
    
    return dummy.next

def print_linked_list(head):
    vals=[]
    while head:
        vals.append(head.val)
        head=head.next
    
    print(vals)

sol=Solution()
l1=build_linked_list([1, 2, 4])
l2=build_linked_list([1, 3, 4])
merged=sol.mergeTwoLists(l1, l2)
print_linked_list(merged)