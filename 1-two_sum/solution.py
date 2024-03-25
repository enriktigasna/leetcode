# Beats 50% memory
# Beats 50% runtime

# Pretty much default solution

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevValues = []
        for i, j in enumerate(nums):
            neededValue = target - j
            if neededValue in nums and nums.index(neededValue) != i:
                return [i, nums.index(neededValue)]