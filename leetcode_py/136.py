from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict = {}
        for i in nums:
            if i in num_dict:
                num_dict[i] += 1
            else:
                num_dict[i] = 1
        
        for key, value in num_dict.items():
            if value == 1:
                return key


            