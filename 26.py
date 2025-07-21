from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        slow = 0  
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]  
        
        return slow + 1  


sol = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = sol.removeDuplicates(nums)
print(k)        
print(nums[:k]) 
