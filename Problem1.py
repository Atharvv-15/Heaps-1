# 215. Kth Largest Element in an Array
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        n = len(nums)
        result = float('inf')

        for i in range(n-k):
            heapq.heappush(heap,-nums[i])

        for i in range(n-k,len(nums)):
            heapq.heappush(heap,-nums[i])
            pop = heapq.heappop(heap)
            result = min(-pop,result)

        return result


        