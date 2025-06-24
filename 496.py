
def nextGreaterElement( nums1, nums2) :
        rest=list()
        for i in nums1:
            flag=False
            for j in nums2:
                if i == j:
                    flag=True

                elif flag and j >= i:
                    rest.append(j)
                    break
                
            else:
                    rest.append(-1)

        return rest
    
nums1=[4,1,2]
nums2=[1,3,4,2]
print(nextGreaterElement(nums1,nums2))
