##2025.8.29
##关于栈的复习
class mystack:
    def __init__(self):
        self.items=[]
    
    def isempty(self):
        return self.items==[]
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
