class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_list = list(secret)
        guess_list = list(guess)
        A = 0
        B = 0
        i = 0
        while i < len(secret_list):
            if secret_list[i] == guess_list[i]:
                A += 1
                secret_list.pop(i)
                guess_list.pop(i)
            else:
                i += 1
        j = 0
        while j < len(guess_list):
            if guess_list[j] in secret_list:
                B += 1
                secret_list.remove(guess_list[j])
            j += 1
        return '{}A{}B'.format(A, B)
