# -*- coding: utf-8 -*-
"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
"""


class ListNode(object):

    def __init__(self, val, next=None):

        self.val = val
        self.next = next


class Solution(object):

    def add_two_numbers(self, l_node1: ListNode, l_node2: ListNode):
        """
        :param l_node1:
        :param l_node2:
        :return:
        """
        return self.add(l_node1, l_node2, 0)

    def add(self, l_node1, l_node2, carry):
        if l_node1 is None and l_node2 is None and carry == 0:
            return None

        value = (l_node1.val if l_node1.val else 0) + (l_node2.val if l_node2.val else 0) + carry
        current = ListNode(value % 10, None)
        current.next = self.add(
            (None if l_node1 is None else l_node1.next),
            (None if l_node2 is None else l_node2.next),
            int(value / 10)
        )
        return current

    @staticmethod
    def add_two_numbers_2(l_node1: ListNode, l_node2: ListNode):
        head = point = ListNode(0)
        carry = 0
        while l_node1 or l_node2:
            new_point = ListNode(0)
            if not l_node1:
                sum_ = l_node2.val + carry
                new_point.val = sum_ % 10
                carry = sum_ // 10
                l_node2 = l_node2.next
            elif not l_node2:
                sum_ = l_node1.val + carry
                new_point.val = sum_ % 10
                carry = sum_ // 10
                l_node1 = l_node1.next
            else:
                sum_ = l_node1.val + l_node2.val + carry
                new_point.val = sum_ % 10
                carry = sum_ // 10
                l_node1 = l_node1.next
                l_node2 = l_node2.next

            point.next = new_point
            point = point.next
        if carry:
            new_point = ListNode(1)
            point.next = new_point
        return head.next


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3, None)))
    l2 = ListNode(5, ListNode(6, ListNode(4, None)))
    l_node = Solution().add_two_numbers(l1, l2)
    print([l_node.val, l_node.next.val, l_node.next.next.val])
    
    l_node_2 = Solution().add_two_numbers_2(l1, l2)
    print([l_node_2.val, l_node_2.next.val, l_node_2.next.next.val])
