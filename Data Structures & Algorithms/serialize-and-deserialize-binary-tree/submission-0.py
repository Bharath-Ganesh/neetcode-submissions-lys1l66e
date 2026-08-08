# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def serialize(self, root):
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if not node:
                res.append('N')
                continue
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        return ",".join(res)

    def deserialize(self, data):
        if not data:
            return None
        node_arr = data.split(",")
        if node_arr[0] == 'N':
            return None
        n = len(node_arr)
        rootNode = TreeNode(int(node_arr[0]))
        queue = deque([rootNode])
        idx = 1
        while queue and idx < n:
            node = queue.popleft()
            if idx < n and node_arr[idx] != 'N':
                leftNode = TreeNode(int(node_arr[idx]))
                node.left = leftNode
                queue.append(leftNode)
            idx += 1

            if idx < n and node_arr[idx] != 'N':
                rightNode = TreeNode(int(node_arr[idx]))
                node.right = rightNode
                queue.append(rightNode)
            idx += 1

        return rootNode
