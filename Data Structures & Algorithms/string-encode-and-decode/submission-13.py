class Solution:
    def __init__(self):
        self.DELIMITER = '#'

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            length = len(word)
            res.append(str(length))
            res.append(self.DELIMITER)
            res.append(word)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        idx, n = 0, len(s)
        if n == 0:
            return []
        res = []
        # 01234567890123
        # 5#Hello5#World
        while idx < n:
            delimiter_index = s.index(self.DELIMITER, idx) #  1
            word_length = int(s[idx:delimiter_index])      # 5
            idx = delimiter_index + 1                      # 2
            word = s[idx: idx + word_length]               # 7
            res.append(word)
            idx += word_length                             # 7
            
        return res