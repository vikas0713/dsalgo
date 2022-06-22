"""Binary tree """


class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None





"""
Tree structure:

            a
           /  \
          b    c
         / \   / \
        d   e  f  g

"""

root_node = TreeNode("a")
b = root_node.left = TreeNode("b")
c = root_node.right = TreeNode("c")
# Level 1
b.left = TreeNode("d")
b.right = TreeNode("e")
# Level 1
c.left = TreeNode("f")
c.right = TreeNode("g")
