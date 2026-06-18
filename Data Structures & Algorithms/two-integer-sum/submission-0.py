class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_values = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen_values:
                return [seen_values[complement], i]
            seen_values[num] = i
        return 0                 
            
