class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:

        # ---First Solution---:

        # Brute Force O(n^2)


        # ---Second Solution---:
        ans = [0 for _ in range(len(heights))]
        stack = []

        for i in range(len(heights)-1,-1,-1):
            visible = 0

            while stack and stack[-1] < heights[i]:
                visible += 1
                stack.pop()
            
            if stack:
                visible += 1
            
            ans[i] = visible
            stack.append(heights[i])
            
        return ans



# ---TEST---
heights1 = [10,6,8,5,11,9]
heights2 = [5,1,2,3,10]

s = Solution()
print(s.canSeePersonsCount(heights1))
print(s.canSeePersonsCount(heights2))
print(s.canSeePersonsCount(heights2))
