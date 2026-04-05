class Solution:
    # dummy_input = ["Hello","World"]
    # 4#Hello5#World

    def __init__(self):
        self.DELIMITER = '#'

    def encode(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ""

        encoded_arr = []
        for word in strs:
            length = len(word)
            encoded_arr.append(str(length))
            encoded_arr.append(str(self.DELIMITER))
            encoded_arr.append(word)
        return "".join(encoded_arr)

    def decode(self, s: str) -> List[str]:
        if not s or s == "":
            return []
        
        idx = 0
        # 4#Hello5#World
        res = []
        while idx < len(s):
            idx_delim = s.index(self.DELIMITER, idx)
            num_digit = int(s[idx: idx_delim])
            res.append(s[idx_delim + 1: idx_delim + 1 + num_digit])
            idx = idx_delim + 1 + num_digit
        return res

















