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

        adjList = defaultdict(list)
        total_words = len(words)
        indegree = defaultdict(int)

        for idx in range(total_words - 1):
            first_word = words[idx]
            second_word = words[idx + 1]
            min_length = min(len(first_word), len(second_word))
            i = 0
            while i < min_length:
                if first_word[i] != second_word[i]:
                    idx1 = ord(first_word[i]) - ord('a')
                    idx2 = ord(second_word[i]) - ord('a')
                    adjList[idx1].append(idx2)
                    indegree[idx2] += 1
                    if idx1 not in indegree:
                        indegree[idx1] = 0
                    break
                i += 1
            if i == min_length and first_word[:min_length] == second_word[:min_length] and len(first_word) > len(
                    second_word):
                return ""

        queue = deque()
        for key, val in indegree.items():
            if val == 0:
                queue.append(key)

        res = []
        while queue:
            key = queue.popleft()
            res.append(chr(ord('a') + key))
            for adjNode in adjList[key]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    queue.append(adjNode)

        return "".join(res)


if __name__ == '__main__':
    s = Solution()
    ans = s.foreignDictionary(["hrn","hrf","er","enn","rfnn"])
    print(ans)