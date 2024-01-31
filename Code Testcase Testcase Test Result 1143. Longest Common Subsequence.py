class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        import numpy as np
        text1_length = len(text1)
        text2_length = len(text2)
        m= np.zeros((len(text1),len(text2)))

        
        
        for i in range(text2_length):
            if text2[i] == text1[0]:
                m[0][i] = 1
            else:
                if i > 0:
                    m[0][i] = m[0][i-1]
            
        for i in range(text1_length):
            if text1[i] == text2[0]:
                m[i][0] = 1
            else:
                if i > 0:
                    m[i][0] = m[i-1][0]
        
        
        for i in range(1,text1_length):
            for j in range(1,text2_length):
                m_max = max(m[i][j-1],m[i-1][j-1],m[i-1][j])
                if(text1[i] == text2[j]):
                    m[i][j] = 1 + m[i-1][j-1]
                else:
                    m[i][j] = max(m[i][j-1],m[i-1][j-1],m[i-1][j])
        print(m)
        return int(max(m[text1_length-1]))
