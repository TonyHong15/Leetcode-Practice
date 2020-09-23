class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    if l1.val == 0 and l2.val == 0 and l1.next is None and l2.next is None:
        return ListNode()
    elif l1.val == 0 and l1.next is None:
        return l2
    elif l2.val == 0 and l2.next is None:
        return l1
    elif l1.next is None and l2.next is None:
        num = l1.val + l2.val
        l3 = ListNode()
        l3.val = num % 10
        if num >= 10:
            l4 = ListNode(1, None)
            l3.next = l4
        return l3
    else:
        l3 = ListNode()
        curr1 = l1
        curr2 = l2
        curr3 = l3
        carry = 0

        while curr1 is not None or curr2 is not None:
            if curr1 is None:
                num = curr2.val + carry
                curr2 = curr2.next
            elif curr2 is None:
                num = curr1.val + carry
                curr1 = curr1.next
            else:
                num = curr1.val + curr2.val + carry
                curr1 = curr1.next
                curr2 = curr2.next
            curr3.val = num % 10
            if num >= 10:
                carry = 1
            else:
                carry = 0
            if curr1 is not None or curr2 is not None:
                temp = ListNode()
                curr3.next = temp
                curr3 = temp
            if carry == 1 and curr1 is None and curr2 is None:
                temp = ListNode(1)
                curr3.next = temp

        return l3


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)
    l7 = ListNode(7)
    l8 = ListNode(8)
    l9 = ListNode(9)

    l1.next = l9
    l2.next = l8
    l9.next = l7
    l8.next = l6
    l7.next = l4
    l6.next = l5
    l5.next = l3
    listing = addTwoNumbers(l1, l2)
    curr = listing
    while curr is not None:
        print(curr.val)
        curr = curr.next
