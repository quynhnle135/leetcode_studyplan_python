class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def print_list(self, head):
        cur = head
        while cur:
            print(cur.val, end=" ")
            cur = cur.next
        print()

    def reverse_linkedlist(self, head):
        cur_node = head
        prev = None
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = next_node
        return prev


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
my_solution = Solution()
my_solution.print_list(head=head)
my_solution.print_list(head=(my_solution.reverse_linkedlist(head=head)))