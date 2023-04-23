class Solution(object):
    def twoSum(self, nums, target):
        nums_dict = {}
        for i in range(0, len(nums)):
            if (target - nums[i]) in nums_dict:
                return [nums_dict[target - nums[i]], i]
            else:
                nums_dict[nums[i]] = i
        return [-1, -1]


my_solution = Solution()

nums1 = [2, 7, 11, 15]
target1 = 9
print(my_solution.twoSum(nums1, target1))

nums2 = [3, 2, 4]
target2 = 6
print(my_solution.twoSum(nums2, target2))

nums3 = [3, 3]
target3 = 6
print(my_solution.twoSum(nums3, target3))
