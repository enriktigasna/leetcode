# Beats 73.71% in runtime

class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Check if it's the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Build the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak