class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
         return False
        
        # Fixed-size array for 26 lowercase letters
        count = [0] * 26
    
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        # If all frequencies are 0, it's a valid anagram
        return all(x == 0 for x in count)
