class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def invertTree(A):
    if A is None: return None
    
    invertTree(A.left)
    invertTree(A.right)
    
    temp = A.left
    A.left = A.right
    A.right = temp
    
    return A

root = Node(100)
root.left = Node(29)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(invertTree(root))