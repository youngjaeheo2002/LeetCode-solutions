class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        import numpy as np
        nums.reverse()
        print(nums)
        m = np.zeros(len(nums))

        m[0] = nums[0]

        if len(nums) >= 2:
            m[1] = max(m[0],nums[1])


        for i in range(1,len(nums)):
            for j in range(0,i-1):
                m[i] = max(nums[i]+m[j],m[i])

            print(m)

        return int(max(m))

