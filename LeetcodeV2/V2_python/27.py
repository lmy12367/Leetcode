class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        slow = 0
        
        for fast in range(len(nums)):

            if nums[fast] != val:

                nums[slow] = nums[fast]
                slow += 1
                

        return slow
    

if __name__ == "__main__":
    solution = Solution()


    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = solution.removeElement(nums1, val1)
    print(f"案例 1 返回长度: {k1}")

    print(f"案例 1 修改后的前 k 个元素: {nums1[:k1]}")
    print("-" * 20)


    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = solution.removeElement(nums2, val2)
    print(f"案例 2 返回长度: {k2}")
    print(f"案例 2 修改后的前 k 个元素: {nums2[:k2]}")