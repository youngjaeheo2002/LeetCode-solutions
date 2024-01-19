class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        import numpy as np

        m_max = np.zeros(len(nums))
        m_min = np.zeros(len(nums))
        m_max[0] = nums[0]
        
        m_min[0] = nums[0]
        for i in range(1,len(nums)):
            m_max[i] = max(m_max[i-1]*nums[i],m_min[i-1]*nums[i],nums[i])
            m_min[i] = min(m_max[i-1]*nums[i],m_min[i-1]*nums[i],nums[i])

        return int(max(m_max))
             
