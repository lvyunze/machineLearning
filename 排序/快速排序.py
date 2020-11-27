def quick_sort(s):
    """快速排序，s为列表"""
    # 结束条件
    if len(s) < 2:
        return
    # 从列表取出一个元素作为基准值
    p = s[0]
    L = [] # 小于
    E = [] # 等于
    R = [] # 大于
    # 把s里的元素放入3个队列
    while len(s) > 0:
        if s[-1] < p:
            L.append(s.pop())
        elif s[-1] == p:
            E.append(s.pop())
        else:
            R.append(s.pop())

    quick_sort(L)
    quick_sort(R)
    s.extend(L)
    s.extend(E)
    s.extend(R)


if __name__ == '__main__':
    s = [1, 7, 3, 5, 4]
    quick_sort(s)
    print(s)