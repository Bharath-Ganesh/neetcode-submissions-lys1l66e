class DisjointSet:

    def __init__(self, n):
        self.size   = [1] * (n + 1)
        self.parent = [ parent_idx for parent_idx in range(n + 1)]

    def findUltimateParent(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findUltimateParent(self.parent[node])
        return self.parent[node]

    def addNodes(self, u, v):
        pu = self.findUltimateParent(u)
        pv = self.findUltimateParent(v)
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

        dis = DisjointSet(n)
        for edge in edges:
            u, v = edge[0], edge[1]
            if not dis.isConnected(u, v):
                dis.addNodes(u, v)

        disconnected_set = set()
        for node in range(n):
            disconnected_set.add(dis.findUltimateParent(node))

        return len(disconnected_set)

















        