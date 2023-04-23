class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        if head is None:
            return head
        dummy_head = ListNode()
        dummy_head.next = head
        cur = dummy_head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_head.next

    def print_list(self, head):
        temp = head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
my_solution = Solution()
my_solution.print_list(head=head)

new_head = my_solution.removeElements(head=head, val=3)
my_solution.print_list(head=new_head)

