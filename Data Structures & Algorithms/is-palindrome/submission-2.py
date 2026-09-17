class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        reverse = ""
        fwd = ""
    
        for i in range(length):
            if s[i].isalnum():
                fwd += s[i].lower()
            if s[length - i - 1].isalnum():
                reverse += s[length - i - 1].lower()
        
        return fwd == reverse