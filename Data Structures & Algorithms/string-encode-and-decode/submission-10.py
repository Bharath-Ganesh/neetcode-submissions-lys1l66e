from typing import List


class Solution:
    """
    Input: ["neet","code","love","you"]

    4#neet4#code4#love#3you
    4neetcode4love3you
    """

    def __init__(self):
        self.DELIMITER = '#'

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            length = len(word)
            res = res + str(length) + self.DELIMITER + word
        return res

    def decode(self, word) -> List[str]:
        if word == "":
            return []

        res = []
        length_of_word_in_str = ""
        index = 0
        while index < len(word):
            ch = word[index]
            if ch == self.DELIMITER:
                length = int(length_of_word_in_str)
                length_of_word_in_str = ""
                index += 1
                res.append(word[index:index + length])
                index += length
            else:
                length_of_word_in_str += ch
                index += 1
        return res

if __name__ == '__main__':
    solution = Solution()
    strs = ["neet","code","love","you"]
    decode= solution.encode(strs)
    print(decode)
    print(solution.decode(decode))