class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # ---My Solution---:

        i = 0
        j = 0
        lenth = 0
        substring = set([])

        while j < len(s):
            
            # not repeat
            if s[j] not in substring:
                substring.add(s[j])
            # found repeat
            else:
                while s[i] != s[j] and i <= j:
                    i += 1
                # update substring
                substring = set([s[k] for k in range(i,j+1)])
                i += 1
            
            lenth = max(lenth, j-i+1)
            j += 1

        return lenth
    
        # ---Better Solution---:
        charSet = set()
        i = 0
        res = 0

        for j in range(len(s)):
            while s[j] in charSet:
                charSet.remove(s[i])
                i += 1
            charSet.add(s[j])
            res = max(res, j-i+1)

        return lenth

# ---TEST---
s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
s4 = "tmmzuxt"

s = Solution()
print(s.lengthOfLongestSubstring(s1))
print(s.lengthOfLongestSubstring(s2))
print(s.lengthOfLongestSubstring(s3))
print(s.lengthOfLongestSubstring(s4))