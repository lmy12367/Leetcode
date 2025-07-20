from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

    

class Solution2:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)  

        for i in range(n):   
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans



sol = Solution()
print(sol.getConcatenation([1, 2, 1]))  
sol1 = Solution2()
print(sol1.getConcatenation([1, 2, 1]))  