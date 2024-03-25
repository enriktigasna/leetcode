# Beats 63.27% Runtime
# Beats 78.32% Memory


import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = [[n] for n, i in enumerate(nums)]
        output = []
        n = len(nums)
        while stack:
            current = stack.pop()
            output.append([nums[i] for i in current])
            for i in range(current[-1] + 1, n):
                to_add = copy.deepcopy(current)
                to_add.append(i)
                if i < n:
                    stack.append(to_add)
        
        output.append([])
        return output