import heapq
def findKthLargest(nums, k):
    maxhead=[]
    heapq.heapify(maxhead)

    for num in nums:
        heapq.heappush(maxhead,num * -1)

    while k>1:
        heapq.heappop(maxhead)
        k=k-1

    return heapq.heappop(maxhead)*-1


num1=[3,2,1,5,6,4]
print(findKthLargest(num1,2))