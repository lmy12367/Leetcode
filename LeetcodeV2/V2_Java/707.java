public class MyLinkedList {
    class ListNode{
        int val;
        ListNode next;
        ListNode(int val){
            this.val=val;
            this.next=null;
        }
    }

    int size;
    ListNode dummyHead;

    public MyLinkedList(){
        size=0;
        dummyHead =new ListNode(0);
    }

    public int get(int index){
        if(index<0||index>=size){
            return -1;
        }

        ListNode cur=dummyHead.next;

        for(int i=0;i<index;i++){
            cur=cur.next;
        }

        return cur.val;
    }

    public void addAtHead(int val){
        addAtIndex(0,val);
    }
    
    public void addAtTail(int val){
        addAtIndex(size,val);
    }

    public void addAtIndex(int index,int val){
        if(index>size) return;
        if(index<0) index=0;

        size++;

        ListNode pred=dummyHead;
        for(int i=0;i<index;i++){
            pred=pred.next;
        }

        ListNode toAdd = new ListNode(val);
        toAdd.next = pred.next;
        pred.next = toAdd;
    }

    public void deleteAtIndex(int index) {
        if (index < 0 || index >= size) {
            return;
        }
        
        size--; 
        
        ListNode pred = dummyHead;
        for (int i = 0; i < index; i++) {
            pred = pred.next;
        }
        
        pred.next = pred.next.next;
    }

}