class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance = [[maxsize]*n for _ in range(n)]
        for i in range(n):
            distance[i][i] = 0
        for a, b, w in edges:
            distance[a][b] = distance[b][a] = w
        for k, i, j in product(range(n), repeat = 3):
            distance[i][j] = min(distance[i][k] + distance[k][j], distance[i][j])
        return min(range(n-1, -1, -1), key = lambda i: sum(d <= distanceThreshold for d in distance[i]))
