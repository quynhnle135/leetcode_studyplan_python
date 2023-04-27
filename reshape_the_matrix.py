class Solution(object):
    def reshapeMatrix(self, mat, r, c):
        nums = []
        for i in range(0, len(mat)):
            for j in range(0, len(mat[i])):
                nums.append(mat[i][j])
        if (r * c) != len(nums):
            return mat
        result = []
        idx = 0
        for row_index in range(r):
            new_arr = []
            for column_index in range(c):
                new_arr.append(nums[idx])
                idx += 1
            result.append(new_arr)
        return result


my_solution = Solution()
res = my_solution.reshapeMatrix(mat=[[1, 2], [3, 4], [5, 6]], r=2, c=3)
print(res)