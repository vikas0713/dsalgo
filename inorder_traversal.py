"""
In order traversal

Left -> root --> Right

Tree structure

            a
           /  \
          b    c
         / \   / \
        d   e  f  g

Time Complexity : O(n)
Space Complexity: O(n)
"""
from binary_tree import root_node


def inorder_traversal(node):
    if not node:
        return
    inorder_traversal(node.left)
    print(node.value)
    inorder_traversal(node.right)


inorder_traversal(root_node)
