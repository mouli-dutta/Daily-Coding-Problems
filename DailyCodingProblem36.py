# Good morning! Here's your coding interview problem for today.

# This problem was asked by Dropbox.

# Given the root to a binary search tree, find the second largest node in the tree.

class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

def insert(root, data):
    if not root:
        return BTNode(data)

    if root.data < data:
        root.right = insert(root.right, data)
    else:
        root.left = insert(root.left, data)

    return root


def second_largest(root):
    if not root or (not root.left and not root.right):
        return -1

    parent = None
    curr = root
    
    # Traverse down to the largest (rightmost) node keeping track of it's parent
    while curr.right:
        parent = curr
        curr = curr.right
    
    # If the rightmost node has no left child, return the parent node
    if not curr.left:
        return parent.data
    
    # If the rightmost node has a left child, traverse down to the rightmost
    # node of the left child
    curr = curr.left
    while curr.right:
        curr = curr.right
    
    # Return the value of the second largest node
    return curr.data
    

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" -> ")
        inorder(root.right)


# test
root = BTNode(5)
insert(root, 3)
insert(root, 34)
insert(root, 8)
insert(root, 9)
insert(root, 1)
insert(root, 10)

print("Second largest root of the BST is ", second_largest(root), sep=": ")

print("Inorder traversal of the tree:")
inorder(root)