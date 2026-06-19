class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for letter in s:
            if letter.isalnum(): # checks if character is a letter or number automatically
                clean += letter.lower() # using += to append; this is all that is needed for this case 

        backward = ""
        for letter in clean: # loop through our cleaned up variable 
            backward = letter + backward # python builds the string in this exact order - letter on left, then current backward string; appends onto front
        
        return clean == backward