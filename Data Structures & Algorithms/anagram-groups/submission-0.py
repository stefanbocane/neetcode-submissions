class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        answer = {} # create empty dict 

        for s in strs:
            # sort the string which will create our key 
            key = "".join(sorted(s)) 
            # this sorts the string (alphabetical) then joins together in a hashable, single string. "-" would give c-a-t

            if key not in answer: # check does key exist in the dict already?
                answer[key] = [] # if not, create a new entry at the new key, empty list 
        
            answer[key].append(s) # otherwise, append onto the correct key the current string
    
        return list(answer.values()) # convert into a list and return - it asks for a list in function def, not a dict