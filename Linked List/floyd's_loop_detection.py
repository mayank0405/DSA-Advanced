class Node:
    def __init__(self, k):
        self.data = k
        self.next = None


def loop_detect(head, k):
    if not head:
        return head
    
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False