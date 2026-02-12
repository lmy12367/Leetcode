from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length=len(nums)
        for i in range(length):
            for j in range(i+1,length):
                if nums[i]+nums[j]==target:
                    return [i,j]
        
        return []
    

test=Solution()
print(test.twoSum(nums = [2,7,11,15], target = 9))
