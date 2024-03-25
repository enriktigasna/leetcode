# Beats 85.20%

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Made based on the algorithm and drawn explanation in neetcode video

        output = [] 

        # First prefix is always 1 since we can't have any numbers before
        output.append(1)
        # Add prefixes into array
        for i in range(len(nums) - 1):
            output.append(nums[i]*output[i])

        # Multiply in postfixes into array
        post = 1
        for i in reversed(range(len(nums))):
            output[i] = output[i]*post
            post = post*nums[i]

        return output