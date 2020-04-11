class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = S.upper()
        s = s.split('-')
        s =''.join(s)[::-1]
        res = []
        while len(s) >= K:
            res.append(s[:K])
            s = s[K:]
        while s:
            res.append(s)
            break
        res = '-'.join(res)[::-1]
        return res
