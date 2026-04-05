class DisjointSets:

    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank   = [0] * (n + 1)
    
    def findUltimateParent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findUltimateParent(self.parent[node])
        return self.parent[node]
    
    def unionByRank(self, u, v):
        pu = self.findUltimateParent(u)
        pv = self.findUltimateParent(v)
        if pu == pv:
            return
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
            self.rank[pu] += 1
        elif self.rank[pu] < self.rank[pv]: 
            self.parent[pu] = pv
            self.rank[pv] += 1
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1
    
    def areConnected(self, u, v):
        pu = self.findUltimateParent(u)
        pv = self.findUltimateParent(v)
        return pu == pv

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        1. For a graph to be tree
        1. No cycle dependency
        2. All nodes need to be reachable or only one component
        1.
           0
          / \ \  
         1   2 3
         /
        4

         0
         / 
         1 => 3 [cycle]
         /
         2
         /
         3
        """
        disjointSets = DisjointSets(n)
        for u, v in edges:
            if not disjointSets.areConnected(u, v):
                disjointSets.unionByRank(u, v)
            else:
                return False
        
        total_components = 0
        for node in range(n):
            if disjointSets.parent[node] == node:
                total_components += 1
        return total_components == 1















