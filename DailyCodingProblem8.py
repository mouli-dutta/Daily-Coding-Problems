# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_unival_subtrees(root):
    count = 0
    def is_unival(node):
        nonlocal count
        if not node:
            return True
        left_unival = is_unival(node.left)
        right_unival = is_unival(node.right)
        if (left_unival and right_unival and
            (not node.left or node.left.val == node.val) and
            (not node.right or node.right.val == node.val)):
            count += 1
            return True
        else:
            return False
    is_unival(root)
    return count




def test():
    # Test case 1
    root1 = TreeNode(5)
    root1.left = TreeNode(5)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(5)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(5)
    assert count_unival_subtrees(root1) == 6

    # Test case 2
    root2 = TreeNode(1)
    root2.left = TreeNode(1)
    root2.right = TreeNode(1)
    root2.right.left = TreeNode(1)
    root2.right.right = TreeNode(1)
    assert count_unival_subtrees(root2) == 5

    # Test case 3
    root3 = TreeNode(2)
    root3.left = TreeNode(3)
    root3.right = TreeNode(4)
    root3.left.left = TreeNode(2)
    root3.left.right = TreeNode(2)
    root3.right.left = TreeNode(4)
    root3.right.right = TreeNode(4)
    assert count_unival_subtrees(root3) == 5

    print("All test cases pass")

test()