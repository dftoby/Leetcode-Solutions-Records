class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        time = len(nums) // 3
        fre = {}

        for i in nums:
            fre[i] = fre.get(i,0) + 1

        result = []
        for i in nums:
            if fre.get(i) > time and i not in result:
                result.append(i)

        return result


nums1 = [3,2,3]
nums2 = [1]
nums3 = [1,2]

s = Solution()

print(s.majorityElement(nums1))
print(s.majorityElement(nums2))
print(s.majorityElement(nums3))