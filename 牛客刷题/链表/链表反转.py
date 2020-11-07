""""
链表反转其实就是各个链表的指针的变化
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverse_list(self, head):
        """反转后的头节点是原始链表的尾接节点，也就是next为None的节点"""
        """
        head: 头节点        
        """
        reverse_head = None  # 反转后的链表头节点
        pre_node = None      # 当前节点的前一个节点
        cur_node = head      # 当前节点
        while cur_node is not None:
            next_node = cur_node.next
            if next_node is None:
                reverse_head = cur_node
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = next_node
        return reverse_head


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    print(node1)
    res = Solution().reverse_list(node1)
    print(res.val)
