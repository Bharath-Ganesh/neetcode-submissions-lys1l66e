class Solution:
    def __init__(self):
        self.DELIMITER = '#'

    def encode(self, words: List[str]) -> str:
        res = []
        for word in words:
            length = len(word)
            res.append(str(length))
            res.append(self.DELIMITER)
            res.append(word)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        """
        ["Hello","World"]
        5#Hello5#World
        """
        n = len(s)
        if n == 0:
            return []
        idx = 0
        res = []
        while idx < n:
            delimiter_idx = s.index(self.DELIMITER, idx)
            length = int(s[idx: delimiter_idx])
            res.append(s[delimiter_idx + 1:delimiter_idx + 1 + length])
            idx = delimiter_idx + length + 1
        return res









