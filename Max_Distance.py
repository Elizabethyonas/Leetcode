class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = -float('inf')
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        for i in range(1, len(arrays)):
            ans = max(ans, abs(min_val -arrays[i][-1]), abs(max_val - arrays[i][0]))
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        return ans
