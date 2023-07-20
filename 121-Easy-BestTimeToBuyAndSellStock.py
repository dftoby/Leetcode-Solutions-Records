class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        # ---My Solution: Correct but too long---
        # max_profit = 0

        # for i in range(len(prices)):
        #     sub_lst = prices[i:]
        #     sub_max = max(sub_lst)

        #     if (sub_max - prices[i] > max_profit):
        #         max_profit = sub_max - prices[i]
            
        # return max_profit

        # ---Better Solution: O(n)---
        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit = max(prices[right]-prices[left], max_profit)
            else:
                left = right
            right += 1

        return max_profit


# ---TEST---

prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]

prices_test = [2,4,1]

s = Solution()

print(s.maxProfit(prices1))
print(s.maxProfit(prices2))
print(s.maxProfit(prices_test))