class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next




def removeElements(head, val):

    node=ListNode(0)
    node.next=head
    prenode=node

    while head:
        if head.val == val:
            prenode.next = head.next
        else:
            prenode=prenode.next
        
        head=head.next
    
    return node.next



