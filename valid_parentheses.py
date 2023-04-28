class Solution(object):
    def isValid(self, s):
        open_paren = []
        for i in range(0, len(s)):
            if s[i] in "([{":
                open_paren.append(s[i])
            else:
                if open_paren == []:
                    return False
                elif (s[i] == "]" and open_paren.pop() != "[") or (s[i] == "}" and open_paren.pop() != "{") or (s[i] == ")" and open_paren.pop() != "("):
                    return False
        return open_paren == []


my_solution = Solution()
print(my_solution.isValid(s="({[]})"))
