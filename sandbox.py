s = "leetcode"
my_dict = {}
for i in range(0, len(s)):
    if s[i] not in my_dict:
        my_dict[s[i]] = 1
    else:
        my_dict[s[i]] += 1

for i in my_dict.keys():
    print(i)

print(my_dict)
