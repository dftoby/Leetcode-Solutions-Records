class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        # ---First Solution---:
        #return None

        # ---Second Solution---:

        # O(2n) = O(n)
        
        ans = [1 for _ in range(len(nums))]

        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        
        pstfix = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= pstfix
            pstfix *= nums[i]

        return ans
    
# ---TEST---
nums1 = [1,2,3,4]
nums2 = [-1,1,0,-3,3]

s = Solution()
print(s.productExceptSelf(nums1))
print(s.productExceptSelf(nums2))

