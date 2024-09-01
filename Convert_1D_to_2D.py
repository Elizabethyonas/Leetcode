class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) % n != 0 or len(original) % m != 0 or len(original) // n != m:
            return []
        ans = []
        i = 0
        j = n - 1
        while j < len(original):
            ans.append(original[i:j + 1])
            i = j + 1
            j += n
        return ans
