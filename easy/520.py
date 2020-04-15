class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if ord(word[0]) < 91:
            i = 0
            for w in word:
                if ord(w) < 91:
                    i += 1
            if i == 1 or i == len(word):
                return True
            else:
                return False
        else:
            for w in word:
                if ord(w) < 91:
                    return False
            return True