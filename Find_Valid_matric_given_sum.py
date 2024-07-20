class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        result = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                value = min(rowSum[i], colSum[j])
                result[i][j] = value
                rowSum[i] -= value
                colSum[j] -= value

        return result
