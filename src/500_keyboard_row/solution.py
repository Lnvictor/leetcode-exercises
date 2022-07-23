from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        keyboard = [first, second, third]

        output_arr = []

        for word in words:
            for row in keyboard:
                if all([letter.lower() in row for letter in word]):
                    output_arr.append(word)

        return output_arr


if __name__ == '__main__':
    s = Solution()
    print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
