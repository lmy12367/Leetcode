from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total=nums1+nums2
        number=len(total)
        total.sort()
        if number%2==0:
            return  (total[number//2-1]+total[number//2])/2
        else:
            return float(total[number//2])
        
sol=Solution()
sol1=sol.findMedianSortedArrays([1,2],[3,4])
print(sol1)