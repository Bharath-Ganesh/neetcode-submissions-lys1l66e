class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adjList = [[]for _ in range(n)]
        visited = [False] * n
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(node, parentNode):
            visited[node] = True
            for adjNode in adjList[node]:
                if visited[adjNode]:
                    if adjNode != parentNode:
                        return False
                else:
                    if not dfs(adjNode, node):
                        return False
            
            return True
            
        for node in range(n):
            if not visited[node]:
                node_seen = dfs(node, -1)
                break


        total_visited_nodes = sum(1 if didVisit else 0 for didVisit in visited)
        return True if node_seen and total_visited_nodes == n else False


        