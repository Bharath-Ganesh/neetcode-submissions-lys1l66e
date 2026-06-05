class DisjointSet:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size   = [0] * n
    
    def findUltimateParent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findUltimateParent(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self, u, v):
        pu = self.findUltimateParent(u)
        pv = self.findUltimateParent(v)
        if pu == pv:
            return
        if self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]            

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dis = DisjointSet(n)

        for u, v in edges:
            dis.unionBySize(u, v)

        disconnected_component = 0
        for node in range(n):
            if dis.findUltimateParent(node) == node:
                disconnected_component += 1
        
        return disconnected_component










        