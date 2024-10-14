class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def delete_loop(head, k):
    if not head:
        return
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: #we have got the meeting point.
            break
    #now we will get the start of cycle
    new_slow = head
    while new_slow.next != fast.next:
        new_slow = new_slow.next
        fast = fast.next
    fast.next = None