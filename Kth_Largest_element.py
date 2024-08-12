class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.numsList = nums
        self.k = k
        heapq.heapify(self.numsList)
        while len(self.numsList) > self.k:
            heapq.heappop(self.numsList)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.numsList, val)
        if len(self.numsList) > self.k:
            heappop(self.numsList)
        return self.numsList[0]
        
            



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
