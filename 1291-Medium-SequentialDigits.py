class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        result = []
        low_digits = len(str(low))
        high_digits = len(str(high))

        sequential = "123456789"

        for i in range(low_digits, high_digits+1):
            for j in range(0, len(sequential)-i+1):
                sequential_num = int(sequential[j:j+i])
                # print(sequential_num, i, j, j+low_digits)
                if low <= sequential_num <= high:
                    result.append(sequential_num)
        
        return result

# ---TEST---
low1, high1 = 100, 300
low2, high2 = 1000, 13000

s = Solution()
print(s.sequentialDigits(low1, high1))
print(s.sequentialDigits(low2, high2))
            