class Solution:
    def climbStairs(self, n: int) -> int:
        
        # ---My Solution:---

    
        # ---Better Solution:---

        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one


# ---TEST---
n1 = 2
n2 = 3

s = Solution()

print(s.climbStairs(n1))
print(s.climbStairs(n2))