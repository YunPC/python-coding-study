class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        result = 0
        for stone in stones:
            if stone in jewels_set:
                result += 1
        return result
