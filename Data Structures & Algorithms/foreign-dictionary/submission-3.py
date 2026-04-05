from collections import defaultdict, deque
from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        ["hrn",
         "hrf",
         "er",
         "enn",
         "rfnn"]
         h -> e -> r -> n -> f
         a -> b -> c
         [,1,1,....]
        """
        # 1. Collect all unique chars
        unique_chars = set("".join(words))

        adjList = defaultdict(list)
        total_words = len(words)
        indegree = {c: 0 for c in unique_chars}

        for w1, w2 in zip(words, words[1:]):
            # detect invalid prefix case
            if w1.startswith(w2) and len(w1) > len(w2):
                return ""
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    adjList[c1].append(c2)
                    indegree[c2] += 1
                    break

        # 3. Kahn’s BFS
        queue = deque([c for c, d in indegree.items() if d == 0])
        res = []
        while queue:
            key = queue.popleft()
            res.append(key)
            for adjNode in adjList[key]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    queue.append(adjNode)

        return "".join(res)


if __name__ == '__main__':
    s = Solution()
    ans = s.foreignDictionary(["hrn","hrf","er","enn","rfnn"])
    print(ans)