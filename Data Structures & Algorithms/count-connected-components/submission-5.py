class DisjointSet:

    def __init__(self, n):
        self.size   = [1] * (n + 1)
        self.parent = [ parent_idx for parent_idx in range(n + 1)]

    def findUltimateParent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findUltimateParent(self.parent[node])
        return self.parent[node]

    def findUnionBySize(self, u, v):
        pu = self.findUltimateParent(u)
        pv = self.findUltimateParent(v)
        if pu == pv:
            return
        if self.size[pu] >= self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]

    def isConnected(self, u, v):
        pu = self.findUltimateParent(u)
        pv = self.findUltimateParent(v)        
        if pu == pv:
            return True
        return False

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        obj = DisjointSet(n)
        for u, v in edges:
            obj.findUnionBySize(u, v)

        connectedComponent = 0
        for node in range(n):
            if obj.findUltimateParent(node) == node:
                connectedComponent += 1
        
        return connectedComponent



















        