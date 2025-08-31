from stack_com import mystack

def panChecker(symbolString):
    s=mystack()
    balanced=True
    index=0
    while index <len(symbolString) and balanced:
        symbol=symbolString[index]

        if symbol=='(':
            s.push(symbol)

        else:
            if s.isempty():
                balanced=False
            else:
                s.pop()
        
        index=index+1

    if balanced and s.isempty():
        return True
    else:
        return False

print(panChecker('((()))'))
print(panChecker('((())'))