class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:  # valid tree must have exactly n-1 edges
            return False

        adjList = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in edges:
            indegree[v] += 1
            indegree[u] += 1
            adjList[u].append(v)
            adjList[v].append(u)

        queue = deque()
        for idx, degree in enumerate(indegree):
            if degree == 1:
                queue.append(idx)

        visited = set()
        total_removed = 0

        while queue:
            node = queue.popleft()
            total_removed += 1

            for adjNode in adjList[node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 1:
                    queue.append(adjNode)

        return total_removed == n