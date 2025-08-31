from stack_com import mystack

def perChecker(symbolString):
    s=mystack()
    balanced=True
    index=0

    while index <len(symbolString) and balanced:
        symbol=symbolString[index]

        if symbol in '([{':
            s.push(symbol)

        else:
            if s.isempty():
                balanced=False
            else:
                top=s.pop()
                if not matches(top,symbol):
                    balanced=False
        index=index+1
    
    if balanced and s.isempty():
        return True
    else:
        return False

def matches(open,close):
    opens='([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)

print(perChecker('(({{[][]}[]{{}}})(()))'))
print(perChecker('{[[[](]}'))
        