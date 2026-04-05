class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Write your code here
        adjList = [[] for _ in range(26)]
        indegree = [0] * 26
        visited_char = set()
        for first_word, second_word in zip(words, words[1:]):
            length = len(second_word)
            for idx in range(length):
                if idx == len(first_word):
                    break
                ch_first = first_word[idx]
                ch_second = second_word[idx]
                if ch_first == ch_second:
                    continue
                ord_first = ord(ch_first) - ord('a')
                ord_second = ord(ch_second) - ord('a')
                # ord_first -> ord_second
                adjList[ord_first].append(ord_second)
                indegree[ord_second] += 1
                visited_char.add(ord_first)
                visited_char.add(ord_second)

        queue = deque()
        for value, degree in enumerate(indegree):
            if value in visited_char and degree == 0:
                queue.append(value)

        res = []
        while queue:
            node = queue.popleft()
            res.append(chr(node + ord('a')))
            for adjNode in adjList[node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    queue.append(adjNode)

        return ''.join(res)
        