class DisjointSet:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank   = [0] * (n)

    def findUltimateParent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findUltimateParent(self.parent[node])
        return self.parent[node]

    def findUnionByRank(self, u, v):
        pu = self.findUltimateParent(u)
        pv = self.findUltimateParent(v)
        if pu == pv:
            return
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        elif self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        disjointSet = DisjointSet(n)
        for u, v in edges:
            disjointSet.findUnionByRank(u, v)

        num_components = 0
        for node in range(len(disjointSet.parent)):
            if disjointSet.parent[node] == node:
                num_components += 1

        return num_components















