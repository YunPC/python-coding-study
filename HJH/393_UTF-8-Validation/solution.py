from typing import List
import re

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        data = list(map(lambda x: bin(x)[2:], data))
        data = list(map(lambda x: '0'*(8 - len(x)) + x, data))
        
        one_bit_reg = ["^0"]
        two_bit_reg = ["^110", "^10"]
        three_bit_reg = ["^1110", "^10", "^10"]
        four_bit_reg = ["^11110", "^10", "^10", "^10"]

        curr = 0
        while curr < len(data):
            if re.search("^11110", data[curr]):
                for i in range(4):
                    if curr + i >= len(data) or re.search(four_bit_reg[i], data[curr + i]) is None:
                        return False
                curr += 4
            elif re.search("^1110", data[curr]):
                for i in range(3):
                    if curr + i >= len(data) or re.search(three_bit_reg[i], data[curr + i]) is None:
                        return False
                curr += 3
            elif re.search("^110", data[curr]):
                for i in range(2):
                    if curr + i >= len(data) or re.search(two_bit_reg[i], data[curr + i]) is None:
                        return False
                curr += 2
            elif re.search("^0", data[curr]):
                for i in range(1):
                    if curr + i >= len(data) or re.search(one_bit_reg[i], data[curr + i]) is None:
                        return False
                curr += 1
            else:
                return False
        
            
        return True