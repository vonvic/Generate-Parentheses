_OPT = dict()

def OPT(n: int):
    '''Returns the number of possible valid parentheses combination of
    `n` pairs.'''
    if n in _OPT: return _OPT[n]
    
    # Base Cases
    if n == 0: return ['']
    if n == 1: return ['()']
    
    # Recursive Cases
    L = []
    for i in range(n):
        # each will have their own list, so generate all possible combinations.
        inside = OPT(n-1-i)
        left = OPT(i)
        for s_inside in inside:
            for s_left in left:
                L.append(f'({s_inside}){s_left}')
    _OPT[n] = L # store answer in dict to minimize duplicate recursive calls.
    return L

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return OPT(n)