class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        lookup = defaultdict(list)
        # Collect every character that appears anywhere in the input up front.    
        word_set = set(''.join(words))

        for idx in range(1, len(words) ):
            first_word  = words[idx - 1]
            second_word = words[idx]
            min_length = min(len(first_word), len(second_word))
            if first_word[:min_length] == second_word[:min_length] and len(first_word) > len(second_word):
                return ""
            
            for ch_idx in range(min_length):
                first_word_ch  = first_word[ch_idx]
                second_word_ch = second_word[ch_idx]
                if first_word_ch != second_word_ch:
                    lookup[first_word_ch].append(second_word_ch)
                    break
        
        indegree = {ch: 0 for ch in word_set}
        for src in lookup:
            for dest in lookup[src]:
                indegree[dest] += 1
        
        queue = deque([ch for ch in word_set if indegree[ch] == 0])
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for adjNode in lookup[node]:
                indegree[adjNode] -= 1
                if indegree[adjNode] == 0:
                    queue.append(adjNode)

        if len(res) != len(word_set):
            return ''

        return ''.join(res)

        
        
        