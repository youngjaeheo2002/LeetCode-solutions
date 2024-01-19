class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import numpy as np

        m = np.ones(len(nums))
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j] :
                    m[i] = max(m[i],1+m[j])

                

        return int(max(m))
