from itertools import islice

la = (x for x in range(0, 10))
print(type(la))
for item in islice(la, 0, 10):  # 取下标5-9的元素
    print(item)
