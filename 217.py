def containsDuplicate(nums: List[int]) -> bool:
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