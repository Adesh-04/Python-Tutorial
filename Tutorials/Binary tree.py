
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

obj = Node(10)

obj.left = Node(20)
obj.right = Node(30)
obj.left.left = Node(40)
obj.left.right = Node(50)

def preorder(node, name):
    if node:
        print(node.data, name)
        preorder(node.left , '  <  ' )
        preorder(node.right, '  >  ')

preorder(obj, '  .  ')


# from anytree import Node, RenderTree

# root = Node(10)

# A = Node(34, parent=root)
# B = Node(89, parent=root)
# C = Node(45, parent=A)
# D = Node(50, parent=B)

# for pre, fill, node in RenderTree(root):
#     print("%s%s" % (pre, node.name))