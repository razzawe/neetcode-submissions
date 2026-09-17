class Solution:
    def isPalindrome(self, s: str) -> bool:
     
        str1 = ""
        str2 = ""
        for i in range (len(s)):
            if(s[len(s) - 1 - i].isalnum()):
                str1 += s[len(s) - 1 - i]
            if(s[i].isalnum()):
                str2 += s[i]
 

        return str1.lower() == str2.lower()