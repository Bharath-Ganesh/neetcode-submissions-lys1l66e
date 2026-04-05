class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = [[] for _ in range(26)]
        indegree = [0] * 26
        visited_char = set()

        for first_word, second_word in zip(words, words[1:]):
            length = min(len(first_word), len(second_word))  # ✅
            for idx in range(length):
                ch_first  = first_word[idx]
                ch_second = second_word[idx]
                if ch_first == ch_second:
                    continue
                ord_first  = ord(ch_first)  - ord('a')
                ord_second = ord(ch_second) - ord('a')
                adjList[ord_first].append(ord_second)
                indegree[ord_second] += 1
                visited_char.add(ord_first)
                visited_char.add(ord_second)
                break
            else:
                if len(second_word) < len(first_word):  # ✅ invalid prefix case
                    return ""

        # collect all chars that appear in words
        for word in words:
            for ch in word:
                visited_char.add(ord(ch) - ord('a'))

        queue = deque()
        for value in visited_char:
            if indegree[value] == 0:
                queue.append(value)

        res = []
        print(queue)
        while queue:
            node = queue.popleft()
            res.append(chr(node + ord('a')))
            for adjNode in adjList[node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    queue.append(adjNode)

        if len(res) != len(visited_char):  # ✅ cycle check
            return ""

        return ''.join(res)