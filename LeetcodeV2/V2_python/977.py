from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        
        i, j = 0, n - 1

        count = n - 1
        
        while i <= j:
            left_square = nums[i] * nums[i]
            right_square = nums[j] * nums[j]
            

            if left_square > right_square:
                res[count] = left_square
                i += 1  
            else:
                res[count] = right_square
                j -= 1  
            
            count -= 1 
            
        return res


if __name__ == "__main__":
    sol = Solution()
    
    # 测试用例 1
    case1 = [-4, -1, 0, 3, 10]
    result1 = sol.sortedSquares(case1)
    print(f"测试用例 1 输入: {case1}")
    print(f"测试用例 1 输出: {result1}")
    print("-" * 30)

    # 测试用例 2
    case2 = [-7, -3, 2, 3, 11]
    result2 = sol.sortedSquares(case2)
    print(f"测试用例 2 输入: {case2}")
    print(f"测试用例 2 输出: {result2}")