"""Binary tree pre-order traversal
Depth First Search
Breadth First Search

Root ---> Left --> Right
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


def pre_order_traversal(node):
    if not node:
        return
    print(node.value)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)


pre_order_traversal(root_node)
