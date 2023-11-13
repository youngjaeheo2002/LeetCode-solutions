class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        nums = sorted(nums)
        print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i +1
            k = len(nums)-1
            while (j < k):
                

                if nums[i] + nums[j] + nums[k] > 0:
                    k = k -1

                elif nums[i] + nums[j] + nums[k] < 0:
                    j = j+1

                else:
                    output.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -=1 
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return output
