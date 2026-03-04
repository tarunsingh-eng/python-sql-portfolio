
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def Maxheight(node):
    if node is None:
        return 0
    else:
        leftH = Maxheight(node.left)
        rightH = Maxheight(node.right)
       # print("We are at", node.data)
       # print("", "leftH = ", leftH,">", "rightH = ",rightH," Result=", leftH>rightH)
        if leftH > rightH:
            return leftH+1
        else:
          #  print("rightH+1 = ", rightH+1)
            return rightH+1
        
      # Test the algorithm
root = Node(100)
root.left = Node(29)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print("Height of tree is", (Maxheight(root)))
