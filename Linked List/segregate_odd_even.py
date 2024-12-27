class Node:
    def __init__(self, k):
        self.data = k
        self.next = None

def segregate_odd_even(head):
    if not head:
        return
    os,oe,es,ee = None,None,None,None
    if head.data%2 == 0:
        es = head
        ee = head
    else:
        os = head
        oe = head
    curr = head.next
    while curr:
        x = curr.data
        if x%2 == 0:
            ee.next = curr
            ee = ee.next
        else:
            oe.next = curr
            oe = oe.next

        curr = curr.next
    if os is None or es is None:
        return head
    ee.next = os
    os.next = None
    return es