class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # ---My Solution O(n^2)---:
        fre = {}
        for i in list(set(s)):
            fre[i] = s.count(i)
        
        for j in list(set(t)):
            if j not in fre or t.count(j) < fre[j]:
                return j

# ---TEST---
s1, t1 = "abcd", "abcde"
s2, t2 = "", "y"
s3, t3 = "a", "aa"

s = Solution()
print(s.findTheDifference(s1, t1))
print(s.findTheDifference(s2, t2))
print(s.findTheDifference(s3, t3))