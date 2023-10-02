from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, current_subset):
            result.append(current_subset[:])
            for i in range(start, len(nums)):
                current_subset.append(nums[i]) 
                backtrack(i + 1, current_subset)
                current_subset.pop()
        result = []
        backtrack(0, [])
        return result

