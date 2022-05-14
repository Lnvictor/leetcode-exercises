from math import comb
from typing import List
from collections import deque
from itertools import permutations

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def bracket(leftcount, rightcount, n, pattern, result):
            if(len(pattern) == 2*n):
                result.append(pattern)
                return
            if(leftcount < n):
                bracket(leftcount+1, rightcount, n, pattern+'(', result)
            if(rightcount < leftcount):
                bracket(leftcount, rightcount+1, n, pattern+')', result)
        bracket(0, 0, n, "", result)
        return result
