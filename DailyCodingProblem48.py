# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

# For example, given the following preorder traversal:

# [a, b, d, e, c, f, g]

# And the following inorder traversal:

# [d, b, e, a, f, c, g]

# You should return the following tree:

#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)
    root_index = inorder.index(root_val) 

    left_subtree_inorder = inorder[:root_index] 
    right_subtree_inorder = inorder[root_index + 1:] 

    left_subtree_preorder = preorder[1:1 + len(left_subtree_inorder)]
    right_subtree_preorder = preorder[1 + len(left_subtree_inorder):]

    root.left = build_tree(left_subtree_preorder, left_subtree_inorder)
    root.right = build_tree(right_subtree_preorder, right_subtree_inorder)

    return root

def reconstruct_tree(preorder, inorder):
    return build_tree(preorder, inorder)


def print_tree(root):
    if root is None:
        return
    
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)
    


# test
preorder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
inorder = ['d', 'b', 'e', 'a', 'f', 'c', 'g']

tree = reconstruct_tree(preorder, inorder)

print_tree(tree)
