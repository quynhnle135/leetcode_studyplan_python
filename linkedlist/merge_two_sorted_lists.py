class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        node = ListNode(0)
        dummy_head = node
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
                node = node.next
            else:
                node.next = list2
                list2 = list2.next
                node = node.next
        while list1:
            node.next = list1
            list1 = list1.next
            node = node.next
        while list2:
            node.next = list2
            list2 = list2.next
            node = node.next
        return dummy_head.next

    def printList(self, head):
        temp = head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()


my_solution = Solution()
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(5)
list1.next.next.next.next = ListNode(7)
my_solution.printList(head=list1)

list2 = ListNode(4)
list2.next = ListNode(6)
list2.next.next = ListNode(8)
my_solution.printList(head=list2)
my_solution.printList(my_solution.mergeTwoLists(list1, list2))


