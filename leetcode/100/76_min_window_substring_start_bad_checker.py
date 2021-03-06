class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tDict = {}
        for c in t:
            if c not in tDict:
                tDict[c] = 1
            else:
                tDict[c] += 1
        start = 0
        minlen = len(s) + 1
        smin = ""
        for i in range(len(s)):
            if s[i] in tDict:
                tDict[s[i]] -= 1
                        
            while (start < i) and (s[start] not in tDict or tDict[s[start]] < 0):
                if s[start] not in tDict:
                    start += 1
                elif tDict[s[start]] < 0:
                    tDict[s[start]] += 1
                    start += 1
            valid = True
            for c in tDict:
                if tDict[c] > 0:
                    valid = False
                    break
            if valid:
                if i - start + 1 < minlen:
                    minlen = i - start + 1
                    smin = s[start: i+1]
        return smin