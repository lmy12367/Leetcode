def removeElement(nums, val):
    left = 0
    right = len(nums) - 1
    count = 0
    while left <= right:
        if nums[left] == val:
            while left <= right and nums[right] == val:
                right -= 1
            nums[left] = nums[right]
            right -= 1
        else:
            count += 1
            left += 1
    return count


list1=[1]
removeElement(list1,1)



            


