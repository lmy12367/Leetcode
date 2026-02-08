from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 初始化结果列表，长度与原数组一致
        res = [0] * n
        
        # 定义左右双指针
        i, j = 0, n - 1
        # count 指向结果列表的末尾，从大到小填充
        count = n - 1
        
        while i <= j:
            left_square = nums[i] * nums[i]
            right_square = nums[j] * nums[j]
            
            # 比较左右两端平方的大小
            if left_square > right_square:
                res[count] = left_square
                i += 1  # 左指针向右移
            else:
                res[count] = right_square
                j -= 1  
            
            count -= 1 
            
        return res

# --- 主函数测试 ---
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