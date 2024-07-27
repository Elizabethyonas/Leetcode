class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = {chr(i): {chr(j): inf for j in range(ord('a'), ord('z') + 1)} for i in range(ord('a'), ord('z') + 1)}
        
        # Distance from any node to itself is 0
        for i in range(ord('a'), ord('z') + 1):
            graph[chr(i)][chr(i)] = 0
        
        # Fill the graph with given transformation costs
        for o, c, z in zip(original, changed, cost):
            graph[o][c] = min(graph[o][c], z)
        
        # Apply Floyd-Warshall algorithm to find all pairs shortest paths
        for k in range(ord('a'), ord('z') + 1):
            for i in range(ord('a'), ord('z') + 1):
                for j in range(ord('a'), ord('z') + 1):
                    if graph[chr(i)][chr(k)] < inf and graph[chr(k)][chr(j)] < inf:
                        graph[chr(i)][chr(j)] = min(graph[chr(i)][chr(j)], graph[chr(i)][chr(k)] + graph[chr(k)][chr(j)])
        
        total_cost = 0
        
        # Calculate the total minimum cost to convert source to target
        for s_char, t_char in zip(source, target):
            if graph[s_char][t_char] == inf:
                return -1
            total_cost += graph[s_char][t_char]
        
        return total_cost
