from collections import defaultdict
from typing import List


class Solution:
    def isPalindrome(self, word):
        return word == word[::-1]

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        blank_idx = False
        lastword = defaultdict(list)
        for idx, word in enumerate(words):
            if word == "":
                blank_idx = idx
                continue
            lastword[word[-1]].append([idx, word])

        for idx, word in enumerate(words):
            if word == "":
                continue
            for word2 in lastword[word[0]]:
                if idx == word2[0]:
                    continue
                if self.isPalindrome(word+word2[1]):
                    res.append([idx, word2[0]])
            if blank_idx is not False and self.isPalindrome(word):
                res.append([idx, blank_idx])
                res.append([blank_idx, idx])
        return res


print("a"[0])
