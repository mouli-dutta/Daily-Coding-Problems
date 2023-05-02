# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

# The list is very long, so making more than one pass is prohibitively expensive.

# Do this in constant space and in one pass.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class List:
    def __init__(self):
        self.head = None
        
    def insert_begin(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    
    def remove_kth_last_node(self, k):
        slow = fast = self.head
        
        for i in range(k):
            fast = fast.next
        
        if not fast:
            return self.head.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
                
    
    def printList(self):
        current = self.head
        while current:
            print(f'{current.val} -> ', end='')
            current = current.next
        print('Null')
    


li = List()
li.insert_begin(5)
li.insert_begin(6)
li.insert_begin(9)
li.insert_begin(2)
li.insert_begin(1)
li.insert_begin(3)

print("Given List:")
li.printList()

k = 4
print(f'List after removing the {k}th last node')
li.remove_kth_last_node(k)

li.printList()


