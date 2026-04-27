class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for u, v in edges:
            # u > v
            adjList[u].append(v)
            adjList[v].append(u)

        visited = [False] * n 
        def detect_cycle_undirected_grap(node, parent):
            visited[node] = True
            for adjNode in adjList[node]:
                if visited[adjNode]:
                    if parent != adjNode:
                        return True
                else:
                    if detect_cycle_undirected_grap(adjNode, node):
                        return True
            
            return False

        
        for node in range(n):
            if not visited[node]:
                if detect_cycle_undirected_grap(node, -1):
                    return False
                break

        countNodes = 0
        for node in range(n):
            if visited[node]:
                countNodes += 1
            
        return True if countNodes == n else False



