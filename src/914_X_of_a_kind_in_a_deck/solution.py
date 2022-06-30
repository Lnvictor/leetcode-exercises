class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
        unique_numbers = set(sorted(deck, key=lambda x: deck.count(x)))
        sorted_occ = [deck.count(num) for num in unique_numbers]
        mdc = gcd(*sorted_occ)
        return mdc <= sorted_occ[0] and mdc > 1
