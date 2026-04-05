class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
            0 - [1]
            1 - [0, 2]
            2 - [1, 3]
            4 - [5]
            5 - [4] 
            0 - 1      4 - 5
                |
                2 - 3 
            [[0,1], [1,2], [2,3], [4,5]]
            u -> v  
        """
        adjList : List[List[int]] = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
  

        visited = set()
        connectedcomponents = 0
        for node in range(n):
            if node not in visited:
                self.dfs(node, visited, adjList)
                connectedcomponents += 1
        return connectedcomponents

        

    def dfs(self, node, visited, adjList):
        visited.add(node)
        for adjNode in adjList[node]:
            if adjNode not in visited:
                self.dfs(adjNode, visited, adjList)

    


        