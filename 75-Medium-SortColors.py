class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # ---My Solution---:
        # map = dict([(0,0), (1,0), (2,0)])

        # for i in nums:
        #     map[i] += 1
        
        # count = 0
        # for i in [0,1,2]:
        #     for j in range(map[i]):
        #         nums[count] = i
        #         count += 1
        
        # print(nums)

        # return None

        # ---Better Solution---:

        def swap(nums, i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        low = 0
        mid = 0
        high = len(nums)-1

        while mid <= high:
            if nums[mid] == 0:
                swap(nums, low, mid)
                mid += 1
                low += 1
            elif nums[mid] == 2:
                swap(nums, mid, high)
                high -=1
            else:
                mid += 1
        
        print(nums)

        return None


# ---TEST---
nums1 = [2,0,2,1,1,0]
nums2 = [2,0,1]


s = Solution()
s.sortColors(nums1)
s.sortColors(nums2)
