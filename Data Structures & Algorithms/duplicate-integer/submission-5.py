class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_map = {} # initialize empty map
        for i, num in enumerate(nums): # iterate through list, add each number to map, enumerate returns tuple of index + value ; num is the value in input list, but key in the map ; i is the index of the loop
                if num in number_map:
                    return True # return true if so
                else: # otherwise, add current index to map and iterate
                    number_map[num] = i
        return False # return false if a duplicate is not found