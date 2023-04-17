# from math import inf


def find_max_subarray_i(nums):
    sum = -10000
    for i in range(0, len(nums)):
        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            sum = max(sum, cur_sum)
    return sum


def find_max_subarray_ii(nums):
    sum = -10000
    cur_sum = 0
    for i in range(0, len(nums)):
        cur_sum += nums[i]
        if cur_sum > sum:
            sum = cur_sum

        if cur_sum < 0:
            cur_sum = 0
    return sum

# def find_max_subarray_ii(nums):



nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [5, 4, -1, 7, 8]
nums3 = [1]
nums4 = [-1, 0]
nums5 = [-5, -4, -2, -1]
print(find_max_subarray_i(nums1))
print(find_max_subarray_i(nums2))
print(find_max_subarray_i(nums3))
print(find_max_subarray_i(nums4))
print(find_max_subarray_i(nums5))
