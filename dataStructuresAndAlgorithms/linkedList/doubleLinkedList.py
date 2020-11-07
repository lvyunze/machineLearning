class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    def __init__(self, node):
        self.__head = node

    def is_empty(self):
        """判断链表为空"""
        return self.__head is None

    def length(self):
        """计算链表长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.val, end=" ")
        print("")

    def add(self, item):
        """在链表头部添加元素"""
        node = Node(item)
        if self.is_empty():
            # 假如是空链表，就将__head指向node
            self.__head = node
        else:
            # 将node的尾节点指向__head
            node.next = self.__head
            # 将_head的头节点的prev指向node
            self.__head.prev = node
            # 将__head指向node
            self.__head = node

    def append(self, item):
        """尾部插入元素"""
        node = Node(item)
        if self.is_empty():
            # 假如是空链表，就将__head指向node
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            # 将尾节点cur的next指向node
            cur.next = node
            # 将node的prev指向cur
            node.prev = cur

    def insert(self, pos, item):
        """指定位置添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos-1):
                count += 1
                cur = cur.next
            # 将node的prev指向cur
            node.prev = cur
            # 将node的next指向cur的next
            node.next = cur.next
            # 将cur的下一个节点的pre指向node
            cur.next.prev = node
            # 将cur的下一个节点指向node
            cur.next = node

    def remove(self, item):
        pass
