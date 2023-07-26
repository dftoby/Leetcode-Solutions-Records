class Solution:
    def countSubstrings(self, s: str) -> int:

        # ---My Solution O(N^3)---:

        # def isPalindromic(str):
        #     l = 0
        #     r = len(str)-1

        #     while l < r:
        #         if str[l] != str[r]:
        #             return False
        #         l += 1
        #         r -= 1
        #     return True
        
        # count = 0
        # for l in range(0,len(s)):
        #     for r in range(l+1,len(s)+1):
        #         if isPalindromic(s[l:r]) is True:
        #             count += 1

        # return count

        # ---Better Solution O(N^2)---:

        # Start to compare if it is a Palindrom from the middle
        # For odd length and even length of str seperately
        # "a a a b"

        count = 0

        for i in range(len(s)):

            # counting the odd length
            l = i
            r = i
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            # counting the even length
            l = i
            r = i + 1
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count
    
# ---TEST---
s1 = "abc"
s2 = "aaa"

s = Solution()
print(s.countSubstrings(s1))
print(s.countSubstrings(s2))
