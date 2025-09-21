def moveZeroes(nums) :
    index=0
    for ele in nums:
        if ele !=0:
            nums[index]=ele
            index +=1
    for i in range(index,len(nums)):
        nums[i]=0

    # print(nums)


nums1=[0,1,0,3,12]
nums2=[0]
moveZeroes(nums1)
moveZeroes(nums2)
