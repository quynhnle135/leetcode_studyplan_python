class Solution(object):
    def search_not_optimal(self, matrix, target):
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == target:
                    return True
        return False

    def searchInMatrix(self, matrix, target):
        row = 0
        column = len(matrix[row]) - 1
        while row < len(matrix) and column >= 0:
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                row += 1
            else:
                column -= 1
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 11
my_solution = Solution()
print(my_solution.search_not_optimal(matrix, target))
print(my_solution.searchInMatrix(matrix, target))