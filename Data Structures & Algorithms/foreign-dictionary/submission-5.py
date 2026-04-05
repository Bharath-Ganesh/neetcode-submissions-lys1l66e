class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """


       ["hrn","hrf","er","enn","rfnn"]
        n -> f
        h -> e
        r -> n
        e -> r  
        h -> e -> r -> n -> f


        hrn 
        hrf

        h->
        """
        word_set = set()
        adjList = defaultdict(list)
        indegree = defaultdict(int)
        for first_word, second_word in zip(words, words[1:]):
            for i in range(len(first_word)):
                if i == len(second_word):
                    if first_word[:i] == second_word:
                        return ""
                    break

                if first_word[i] != second_word[i]:
                    # n -> f
                    u = first_word[i]
                    v = second_word[i]
                    adjList[u].append(v)
                    word_set.add(u)
                    word_set.add(v)
                    indegree[v] += 1
                    break
        
        queue = deque()
        for ch in word_set:
            if indegree[ch] == 0:
                queue.append(ch)

        res = []
        while queue:
            ch = queue.popleft()
            res.append(ch)
            for adjCh in adjList[ch]:
                indegree[adjCh] -= 1
                if not indegree[adjCh]:
                    queue.append(adjCh)
        
        return "".join(res) if len(res) == len(word_set) else ""










        

        