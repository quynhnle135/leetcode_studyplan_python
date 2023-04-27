class Solution(object):
    def pascalTriangle(self, numsRow):
        pascal_triangle = [[1]]
        for i in range(1, numsRow):
            prev_row = pascal_triangle[-1]
            new_row = [1]
            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j])
            new_row.append(1)
            pascal_triangle.append(new_row)
        return pascal_triangle



my_solution = Solution()
print(my_solution.pascalTriangle(numsRow=7))