

def containsDuplicate1(nums):
    if len(nums) == 0:
        return False
    
    mapping={}
    for i in nums:
        if i not in mapping:
            mapping[i] = 1

        else:
            mapping[i]=mapping.get(i)+1

    for j in mapping.values():
        if j > 1:
            return True
        
    return False

def containsDuplicate2(nums):
    if nums==None or len(nums)==0:
        return False
    
    hashset=set()

    for num in nums:
        hashset.add(num)
    if len(hashset) == len(nums):
        return False
    else:
        return True

num1=[1,2,3,1]
num2=[1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate2(num1))
print(containsDuplicate2(num2))