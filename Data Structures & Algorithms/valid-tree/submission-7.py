class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # There shouldn't be a cycle : toposort
        # All the nodes are connected
        if n == 1:
            return True

        adjList = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            indegree[v] += 1
            indegree[u] += 1

        visited = set()
        def dfs(rootNode):
            visited.add(rootNode)
            for adjNode in adjList[rootNode]:
                if adjNode not in visited:
                    dfs(adjNode)

        queue = deque()
        for idx, degree in enumerate(indegree):
            if degree == 1:
                queue.append(idx)

        total_nodes = 0
        while queue:
            node = queue.popleft()
            total_nodes += 1
            for adjNode in adjList[node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 1:
                    queue.append(adjNode)
        
        
        if total_nodes != n:
            return False
        dfs(0)
        return True if len(visited) == n else False
    
