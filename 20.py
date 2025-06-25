##解题方法1
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={')':'(',']':'[','}':'{'}

        for char in s:
            if char in dic.values():
                stack.append(char)
            elif char in dic.keys():
                if stack==[] or dic(char) != stack.pop():
                    return False
            else:
                return False
        
        return stack==[]
    
##解题方法1
class Solution1:
    def isValid1(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if c == ')':
                    if temp != '(':
                        return False
                elif c == ']':
                    if temp != '[':
                        return False
                elif c == '}':
                    if temp != '{':
                        return False
        
        return True if len(stack) == 0 else False
