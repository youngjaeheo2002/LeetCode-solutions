class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        def helper(s1,s2):
            if len(s1) != len(s2):
                return False
            dict1 = {}
            dict2 = {}

            for i in range(len(s1)):
                if s1[i] in dict1:
                    dict1[s1[i]] += 1

                else:
                    dict1[s1[i]] = 1

                if s2[i] in dict2:
                    dict2[s2[i]] += 1

                else:
                    dict2[s2[i]] = 1
            return dict1 == dict2

            
        for i in range(len(s2)-length+1):

            substring = s2[i:i+length]
            if helper(s1,substring):
                return True

        return False

