def contain_duplicates_i(nums):
    my_set = set(nums)
    return len(my_set) != len(nums)


def contain_duplicates_ii(nums):
    nums.sort()
    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False



nums1 = [1, 2, 3, 1]
print(contain_duplicates_i(nums1))
print(contain_duplicates_ii(nums1))

nums2 = [1, 2, 3, 4]
print(contain_duplicates_i(nums2))
print(contain_duplicates_ii(nums2))