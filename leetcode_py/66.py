from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
       
        return [1] + [0] * n
    
sol = Solution()
print(sol.plusOne([1,2,3]))  # [1,2,4]
print(sol.plusOne([9,9,9]))  # [1,0,0,0]
print(sol.plusOne([0]))      # [1]
