# Blute force
# class KthLargest:
#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.nums = nums

#     def add(self, val: int) -> int:
#         self.nums.append(val)
#         # return self.nums
#         self.nums=sorted(self.nums)
#         return self.nums[-self.k]

## heapqを使用した解放。これがベスト
class KthLargest(object):
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

        heapq.heapify(self.nums)

        while len(self.nums)>k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums)>self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

