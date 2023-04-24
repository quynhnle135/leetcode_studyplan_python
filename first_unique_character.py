class Solution(object):
    def firstUnique(self, s):
        char_dict = {}
        for i in range(0, len(s)):
            if s[i] not in char_dict:
                char_dict[s[i]] = 1
            else:
                char_dict[s[i]] += 1
        for i in range(0, len(s)):
            if char_dict[s[i]] == 1:
                return i
        return -1


my_solution = Solution()
print(my_solution.firstUnique("hello"))
print(my_solution.firstUnique("leetcode"))
print(my_solution.firstUnique("aaaaaa"))
