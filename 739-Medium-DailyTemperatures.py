class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        # ---First Solution---:

        # Brute Force Search O(n^2)
        # ans = [0 for _ in range(len(temperatures))]

        # for i in range(len(temperatures)):
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             ans[i] = j - i
        #             break

        # return ans

        # ---Second Solution---:
        ans = [0 for _ in range(len(temperatures))]
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                stackT, stackI = stack.pop()
                ans[stackI] = i - stackI
            stack.append([temperatures[i],i])
        return ans



   

# ---TEST---
temperatures1 = [73,74,75,71,69,72,76,73]
temperatures2 = [30,40,50,60]
temperatures3 = [30,60,90]

s = Solution()
print(s.dailyTemperatures(temperatures1))
print(s.dailyTemperatures(temperatures2))
print(s.dailyTemperatures(temperatures3))
