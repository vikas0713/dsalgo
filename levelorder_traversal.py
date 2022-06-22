"""
Level order traversal

level1 --> level2 ----> level3 .......
Tree structure

            a
           /  \
          b    c
         / \   / \
        d   e  f  g

Time Complexity : O(n)
Space Complexity: O(n)
"""

class LinkedList:
    """Queue structure"""
    def __init__(self, value):
        self.head = value
        self.next = None


def leve_lorder_traversal(node):
    if not node:
        return
