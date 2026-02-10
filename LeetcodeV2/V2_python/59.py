class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        
        cur = 1
        target = n * n
        
        while cur <= target:
            for i in range(left, right + 1):
                matrix[top][i] = cur
                cur += 1
            top += 1 
            
            for i in range(top, bottom + 1):
                matrix[i][right] = cur
                cur += 1
            right -= 1 

            for i in range(right, left - 1, -1):
                matrix[bottom][i] = cur
                cur += 1
            bottom -= 1 

            for i in range(bottom, top - 1, -1):
                matrix[i][left] = cur
                cur += 1
            left += 1 
            
        return matrix


if __name__ == "__main__":
    sol = Solution()
    
    print("n = 3:")
    res3 = sol.generateMatrix(3)
    for row in res3: print(row)
    
    print("\nn = 1:")
    res1 = sol.generateMatrix(1)
    for row in res1: print(row)