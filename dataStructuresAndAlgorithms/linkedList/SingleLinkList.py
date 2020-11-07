class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class SingleLinkList(object):
    # 单链表
    """
    1、判断链表是否为空
    2、查看链表长度
    3、查找节点是否存在
    4、遍历整个链表
    5、在链表的头部添加元素
    6、在链表的尾部添加元素
    7、在链表的特定位置插入元素
    8、删除链表中特定的元素
    9、更新链表中特定的元素
    """
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """查看链表的长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def search(self, item):
        """查找结点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.val == item:
                return True
            else:
                return False
        return False

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur is not None:
            print(cur.val, end=' ')
            cur = cur.next
        print("\n")

    def add(self, item):
        """链表头部当中添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部日添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            # 如果pos位置再0或者以前，那么都当做头部插入来
            self.add(item)
        elif pos > self.length() - 1:
            # 如果pos位置比原来的链表长，那么都当作尾插入来
            self.append(item)
        else:
            per = self.__head
            count = 0
            # 直到移动链表指定位置的前置
            while count < pos - 1:
                count += 1
                per = per.next
            # 当循环退出后，pre指向pos-1位置,直接移动链表位置的指向即可
            node = Node(item)
            node.next = per.next
            per.next = node

    def remove(self, item):
        """删除节点,出现两种特殊情况
        1、删除的点是否是头节点
        # 2、删除的节点是尾节点
        """
        cur = self.__head
        pre = None
        while cur is not None:
            # 假如找到了链表当中的这一个值
            if cur.val == item:
                # 先判断此节点是否是头节点,要是需要删除的元素是头节点，就直接让头节点指向cur的next
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                # 删除完成后需要直接退出
                break
            else:
                pre = cur
                cur = cur.next

    def update(self, item, reitem):
        """更新列表元素"""
        cur = self.__head
        while cur is not None:
            if cur.val == item:
                cur.val = reitem
            else:
                cur = cur.next


if __name__ == '__main__':
    l1 = SingleLinkList()
    print(l1.is_empty())
    print(l1.length())
    l1.append(3)
    l1.add(999)
    l1.insert(-3, 110)
    l1.insert(99, 111)
    print(l1.is_empty())
    print(l1.length())
    l1.travel()
    l1.remove(3)
    l1.update(111, 123)
    l1.travel()
