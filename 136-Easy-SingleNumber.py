class Solution:
    def singleNumber(self, nums: list[int]) -> int:

        # ---My Solution---:
        nums.sort()

        for i in range(0,len(nums),2):
            if i == len(nums)-1 or nums[i] != nums[i+1]:
                return nums[i]
        return nums[0]

        # ---Better Solution---:

# ---TEST---
nums1 = [2,2,1]
nums2 = [4,1,2,1,2]
nums3 = [1]

s = Solution()
print(s.singleNumber(nums1))
print(s.singleNumber(nums2))
print(s.singleNumber(nums3))