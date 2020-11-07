class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def merge(self, head1, head2):
        if head1 is None:
            return head2
        elif head2 is None:
            return head1
        if head1.val < head2.val:
            merge_link = head1
            merge_link.next = self.merge(head1.next, head2)
        else:
            merge_link = head2
            merge_link.next = self.merge(head2.next, head1)
        return merge_link


if __name__ == '__main__':
    link_node1 = ListNode(1)
    link_node2 = ListNode(5)
    link_node1.next = link_node2
    link_node3 = ListNode(3)
    link_node4 = ListNode(4)
    link_node3.next = link_node4
    link_node = Solution().merge(link_node1, link_node3)
    while link_node is not None:
        print(link_node.val)
        link_node = link_node.next
