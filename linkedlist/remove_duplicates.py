class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        cur_node = head
        dummy_head = ListNode()
        dummy_head.next = cur_node
        while cur_node and cur_node.next:
            if cur_node.next.val == cur_node.val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        return dummy_head.next

    def print_list(self, head):
        cur = head
        while cur:
            print(cur.val, end=" ")
            cur = cur.next
        print()


head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(3)
head.next.next.next.next.next.next = ListNode(4)

my_solution = Solution()
my_solution.print_list(head=head)
new_head = my_solution.deleteDuplicates(head=head)
my_solution.print_list(head=new_head)



