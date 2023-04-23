def merge(nums1, m, nums2, n):
    res = [0] * len(nums1)
    i = j = k = 0
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            res[k] = nums1[i]
            k += 1
            i += 1
        else:
            res[k] = nums2[j]
            k += 1
            j += 1
    while i < m:
        res[k] = nums1[i]
        k += 1
        i += 1
    while j < n:
        res[k] = nums2[j]
        k += 1
        j += 1

    for i in range(0, len(res)):
        nums1[i] = res[i]


def merge_optimal(nums1, m, nums2, n):
    i = m - 1 # last value in first array
    j = n - 1 # last value in the second array
    k = m + n - 1 # first pos in the first array
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        else:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
# merge(nums1, m, nums2, n)
merge_optimal(nums1, m, nums2, n)
print(nums1)

