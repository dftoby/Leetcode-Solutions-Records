class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        # ---My Solution---:        


        # ---Better Solution O(n)---:

        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum += n
            maxSum = max(curSum, maxSum)

            if curSum < 0:
                curSum = 0
        
        return maxSum



# ---TEST---
nums1 = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [1]
nums3 = [5,4,-1,7,8]

s = Solution()
print(s.maxSubArray(nums1))
print(s.maxSubArray(nums2))
print(s.maxSubArray(nums3))
