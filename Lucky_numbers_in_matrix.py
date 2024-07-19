class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        row = set()
        col = set()
        for i in range(m):
            temp = float('inf')
            for j in range(n):
                temp = min(temp, matrix[i][j])
            row.add(temp)

        for j in range(n):
            temp = -float('inf')
            for i in range(m):
                temp = max(temp, matrix[i][j])
            col.add(temp)
        lucky_numbers = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] in row and matrix[i][j] in col:
                    lucky_numbers.append(matrix[i][j])

        return lucky_numbers
