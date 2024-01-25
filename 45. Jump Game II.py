class Solution:
    def jump(self, nums: List[int]) -> int:
        import numpy as np

        m = np.zeros(len(nums))

        for i in range(len(nums)-2,-1,-1):

            smallest_jump = 10000
            for j in range(i+1,nums[i]+1+i):
                
                if j in range(len(nums)):

                    smallest_jump = min(m[j] + 1 ,smallest_jump)

            m[i] = smallest_jump



        return int(m[0])
