# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

# In this example, assume nodes with the same value are the exact same node objects.

# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def get_len(head: Node):
    len = 0
    while head:
        len += 1
        head = head.next
    return len

def get_intersection_node(headA: Node, headB: Node):
    currA, currB = headA, headB

    # find the lengths of both linked lists
    lenA, lenB = get_len(currA), get_len(currB)

    # traverse the longer linked list by the difference between their lengths
    if lenA > lenB:
        for i in range(lenA - lenB):
            currA = currA.next
    else:
        for i in range(lenB - lenA):
            currB = currB.next

    # traverse both linked lists simultaneously until we find the intersecting node
    while currA and currB:
        if currA.value == currB.value:
            return f'Value of intersecting node: {currA.value}'
        currA = currA.next
        currB = currB.next

    # if there is no intersection, return no solution
    return "No Solution"


# create the linked lists
A = Node(3)
A.next = Node(7)
A.next.next = Node(8)
A.next.next.next = Node(10)

B = Node(99)
B.next = Node(1)
B.next.next = Node(8)
B.next.next.next = Node(10)

print(get_intersection_node(A, B))