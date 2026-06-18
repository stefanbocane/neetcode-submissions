class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        integer_array1 = [ord(char) for char in s]
        integer_array2 = [ord(char) for char in t]
        integer_array1.sort()
        integer_array2.sort()
        
        if integer_array1 == integer_array2:
            return True
        else: 
            return False
        