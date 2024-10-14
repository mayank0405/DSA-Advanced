class Node:
    def __init__(self, k):
        self.data  = k
        self.next = None

def revese_k(head, k):
    if head is None:
        return None
    prev, curr = None,None
    next_node = None
    i = 0
    while curr and i < k:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        i+=1
    if next_node is not None:
        head.next = revese_k(curr, k) #here head is pointing to the last node of the reversed linked list
    return prev