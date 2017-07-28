# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
list1 = [(x, y, z) for x in range(1, 5) for y in range(1, 5) for z in range(1, 5) if x != y != z != x]
print(len(list1))
for i in list1:
    print(i)
