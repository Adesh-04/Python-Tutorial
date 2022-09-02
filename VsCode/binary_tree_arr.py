
class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def array_to_bst(arr):
    if not arr:
        return None
    mid_num = len(arr)//2
    node = Node(arr[mid_num])
    node.left = array_to_bst(arr[:mid_num])
    node.right = array_to_bst(arr[mid_num+1:])
    return node


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

root = array_to_bst([1,2,4,3,5,6,8])
inorder(root)
    
       





