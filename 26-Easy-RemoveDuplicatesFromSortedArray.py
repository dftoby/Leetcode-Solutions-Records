class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        # ---My Solution---:

        current = nums[0]
        next = 1
        count = 1

        for i in range(1,len(nums)):
            if nums[i] > current:
                nums[next] = nums[i]
                next += 1
                current = nums[i]
                count += 1

        return count
        
        # ---Better Solution---:

# ---TEST---
nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]

s = Solution()
print(s.removeDuplicates(nums1))
print(s.removeDuplicates(nums2))
