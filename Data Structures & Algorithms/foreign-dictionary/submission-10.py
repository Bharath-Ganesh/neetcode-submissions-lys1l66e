class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = defaultdict(list)
        indegree = defaultdict(int)
        visited_char = set()

        for word in words:
            for ch in word:
                node = ord(ch) - ord('a')
                visited_char.add(node)
                if node not in indegree:
                    indegree[node] = 0

        for first_word, second_word in zip(words, words[1:]):
            for idx in range(min(len(first_word), len(second_word))):
                if first_word[idx] != second_word[idx]:
                    ord_first = ord(first_word[idx]) - ord('a')
                    ord_second = ord(second_word[idx]) - ord('a')
                    adjList[ord_first].append(ord_second)
                    indegree[ord_second] += 1
                    break
            else:
                if len(first_word) > len(second_word):
                    return ""

        queue = deque()
        for node in visited_char:
            if indegree[node] == 0:
                queue.append(node)

        res = []
        while queue:
            node = queue.popleft()
            res.append(chr(node + ord('a')))
            for adjNode in adjList[node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    queue.append(adjNode)

        if len(res) != len(visited_char):
            return ""
        return ''.join(res)