class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        visited =[False] * n
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        self.dfs(adj, 0, visited)
        for node in range(n):
            if not visited[node]:
                return False
        visited =[False] * n
        if self.detect_cycle_in_directed(adj, 0, -1, visited):
            return False
        return True
    
    def dfs(self, adj, node, visited):
        visited[node] = True
        for adjNode in adj[node]:
            if not visited[adjNode]:
                self.dfs(adj, adjNode, visited)
          

    def detect_cycle_in_directed(self, adj, node, parent, visited):
        visited[node] = True
        for adjNode in adj[node]:
            if not visited[adjNode]:
                if self.detect_cycle_in_directed(adj, adjNode, node, visited):
                    return True
            else:
                if parent != adjNode:
                    return True
        
        return False
