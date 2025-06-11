def findMaxConsecutiveOnes(nums):
    result=0
    count=0
    for ele in nums:
        if ele ==1:
            count+=1
        else:
            if count > result:
                result=count
                count=0

    if count>result:
        result=count
    return result


test=[1,1,0,1,1,1]
test2=[1,0,1,1,0,1]
test3=[1,1,0,1,1,1]
print(findMaxConsecutiveOnes(test))
print(findMaxConsecutiveOnes(test2))
print(findMaxConsecutiveOnes(test3))
