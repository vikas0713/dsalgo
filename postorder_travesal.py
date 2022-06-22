"""
post order traversal

left -> right -> root
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


def postorder_traversal(node):
    if not node:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.value)


postorder_traversal(root_node)
