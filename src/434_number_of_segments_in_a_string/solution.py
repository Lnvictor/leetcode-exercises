class Solution:
    def countSegments(self, s: str) -> int:
        seg_counter = 0
        seg_started = False
        for i, character in enumerate(s):
            if (not seg_started) and character != ' ':
                seg_started = True
            if (character == ' ' or i == len(s) - 1) and seg_started:
                seg_counter += 1
                seg_started = False

        return seg_counter
