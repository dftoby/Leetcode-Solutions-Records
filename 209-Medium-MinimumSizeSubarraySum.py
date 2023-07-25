import sys

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        # ---My Solution---:


        # ---Better Solution O(n)---:
        i = 0
        j = 0
        sum = 0
        mn = sys.maxsize

        while j < len(nums):
            sum += nums[j]

            while sum >= target:
                sum -= nums[i]
                mn = min(mn, j-i+1)
                i += 1
            
            j += 1
        
        if (mn == sys.maxsize):
            return 0
        return mn

# ---TEST---
target1 = 7
nums1 = [2,3,1,2,4,3]

target2 = 4
nums2 = [1,4,4]

target3 = 11
nums3 = [1,1,1,1,1,1,1,1]

s = Solution()
print(s.minSubArrayLen(target1, nums1))
print(s.minSubArrayLen(target2, nums2))
print(s.minSubArrayLen(target3, nums3))
