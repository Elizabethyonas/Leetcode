class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_points = sum(cardPoints)
        n = len(cardPoints)
        window_size = n - k 
        min_window_sum = float('inf')
        current_sum = 0
        for i in range(n):
            current_sum += cardPoints[i]
            if i >= window_size:
                current_sum -= cardPoints[i - window_size]
            if i >= window_size - 1:
                min_window_sum = min(min_window_sum, current_sum)
        return total_points - min_window_sum
