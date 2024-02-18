#https://leetcode.com/problems/word-break/submissions/1178416347/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = [False]*len(s)

        m.append(True)


        start = len(s)-1

        while(start >= 0):
            for word in wordDict:
                if s[start:start+len(word)] == word:
                    m[start] = m[start] or (True and m[start+len(word)])

        
            start -=1
        print(m)
        return m[0]

