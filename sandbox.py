# # s = "leetcode"
# # my_dict = {}
# # for i in range(0, len(s)):
# #     if s[i] not in my_dict:
# #         my_dict[s[i]] = 1
# #     else:
# #         my_dict[s[i]] += 1
# #
# # for i in my_dict.keys():
# #     print(i)
# #
# # print(my_dict)
#
# # nums1 = [1, 2, 3, 4]
# # nums2 = [7, 8, 9, 10]
# # ans = []
# # for i in range(0, len(nums1)):
# #     ans.append(nums1[i])
# #
# # print(ans)
#
# 2D matrix
matrix = [[1, 2], [2, 3], [3, 4]]
# print matrix
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()


nums = [1, 2, 2, 3, 3, 4]
result = []
row = 2
column = 3
idx = 0
for i in range(0, row):
    for j in range(0, column):
        result.append(nums[idx])
        idx += 1
print(result)
