class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # ---My Solution---:
        # p1 = 0
        # p2 = 0

        # result = []

        # while p1 < m:
        #     print(p1,nums1[p1],p2,nums2[p2])
        #     if nums1[p1] < nums2[p2]:
        #         result.append(nums1[p1])
        #         p1 += 1
        #     elif nums1[p1] > nums2[p2]:
        #         result.append(nums2[p2])
        #         p2 += 1
        #     else:
        #         result.append(nums1[p1])
        #         result.append(nums2[p2])
        #         p1 += 1
        #         p2 += 1
        
        # if p2 < n:
        #     result += nums2[p2::]
        
        # nums1 = result
        # print(nums1)

        # return None

        # ---Better Solution---:
        # Inserting nums2 backward from the end of the nums1 backward

        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1
        
        # fill nums2 remaining elements
        while n > 0:
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1
        
        print(nums1)

# ---TEST---
nums11 = [1,2,3,0,0,0]
m1 = 3
nums21 = [2,5,6]
n1 = 3

nums12 = [1]
m2 = 1
nums22 = []
n2 = 0

nums13 = [0]
m3 = 0
nums23 = [1]
n3 = 1

s = Solution()
s.merge(nums11, m1, nums21, n1)
s.merge(nums12, m2, nums22, n2)
s.merge(nums13, m3, nums23, n3)