class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:

        # ---First Solution---:
        # O(NlogN)
        # Not fully functional

        # nums.sort()

        # current = 1

        # for i in range(len(nums)-1):
        #     if nums[i] <= 0:
        #         pass
        #     else:
        #         if nums[i] == current:
        #             current += 1
        #         else:
        #             return current
        # return current+1

        # ---Second Solution---:

    
# ---TEST---
nums1 = [1,2,0]
nums2 = [3,4,-1,1]
nums3 = [7,8,9,11,12]

s = Solution()
print(s.firstMissingPositive(nums1))
print(s.firstMissingPositive(nums2))
print(s.firstMissingPositive(nums3))
