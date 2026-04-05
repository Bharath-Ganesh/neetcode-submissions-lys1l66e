class DisjointSets:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank   = [0] * (n)
    
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
    """
    [0  0   0   0  4  5]
    0 - 1 - 2 - 3

    4 - 5
    """
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        disjointSet = DisjointSets(n)
        for u, v in edges:
            if not disjointSet.areConnected(u, v):
                disjointSet.unionByRank(u, v)

        res = 0
        for node in range(n):
            if disjointSet.parent[node] == node:
                res += 1
        return res
        