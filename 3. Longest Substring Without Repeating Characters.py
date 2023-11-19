class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        i = 0
        j = 1
        max = 1
        while j < len(s):
            print(i,j)
            if s[j] in s[i:j]:
                while(s[j] in s[i:j]):
                    print(i,j)
                    i += 1
                print(i,j)


            else:
                print(i,j)
                length = j-i + 1
                if length > max:
                    max = length

            j += 1

        return max
