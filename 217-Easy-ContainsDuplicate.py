class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # ---My Solution O(n^2)---:
        return len(nums) != len(set(nums))

        # ---Better Solution O(n)---:


# ---TEST---
nums1 = [1,2,3,1]
nums2 = [1,2,3,4]
nums3 = [1,1,1,3,3,4,3,2,4,2]

s = Solution()
print(s.containsDuplicate(nums1))
print(s.containsDuplicate(nums2))
print(s.containsDuplicate(nums3))
