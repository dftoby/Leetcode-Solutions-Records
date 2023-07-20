class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # ---My Solution O(n^2)---:
        # for i in range(0, len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # ---Better Solution O(n)---:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            minus = target - nums[i]
            if minus in hashmap.keys() and i != hashmap[minus]:
                return [i, hashmap[minus]]

# ---TEST---
lst1, num1 = [2,7,11,15],9
lst2, num2 = [3,2,4],6
lst3, num3 = [3,3],6

lst_test, num_test = [2,5,5,11],10

s = Solution()
print(s.twoSum(lst1, num1))
print(s.twoSum(lst2, num2))
print(s.twoSum(lst3, num3))

print(s.twoSum(lst_test, num_test))