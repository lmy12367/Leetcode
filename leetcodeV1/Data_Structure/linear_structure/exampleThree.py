from stack_com import mystack

def baseConverter(decNumber,base):
    digits='0123456789ABCDEF'

    remstack=mystack()

    while decNumber>0:
        rem=decNumber%base
        remstack.push(rem)
        decNumber=decNumber//base

    newString=''

    while not remstack.isempty():
        newString=newString+digits[remstack.pop()]

    return newString

print(baseConverter(25,2))
print(baseConverter(25,16))