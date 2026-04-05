class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = set()
        if self.dfs(adjList, 0, -1, visited):
            return False
        for node in range(n):
            if node not in visited:
                return False
    
        return True
    def dfs(self, adjList, node, parent, visited):
        visited.add(node)

        for adjNode in adjList[node]:
            if adjNode not in visited:
                if self.dfs(adjList, adjNode, node, visited):
                    return True
            else:
                if parent != adjNode:
                    return True
        return False