class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
class dandh:
    def __init__(self,diameter,height):
        self.diameter=diameter
        self.height=height
        
def dnh(root):
    if root==None:
        val=dandh(0,0)
        return val
    left=dnh(root.left)
    right=dnh(root.right)
    leftd=left.diameter
    rightd=right.diameter
    rootd=left.height+right.height+1
    diameter=max(leftd,rightd,rootd)
    height=max(left.height,right.height)+1
    return dandh(diameter,height)
        
def treeinput():
    data=int(input())
    if data==-1:
        return None
    root=BinaryTree(data)
    leftdata=treeinput()
    rightdata=treeinput()
    root.left=leftdata
    root.right=rightdata
    return root
        
def printTree(root):
    if root==None:
        return
    print(root.data,end=":")
    if root.left!=None:
        print("L",root.left.data,end=",")
    if root.right!=None:
        print("R",root.right.data,end="")
    print()
    printTree(root.left)
    printTree(root.right)

    
root=treeinput()
print("BINARY TREE IS :")
printTree(root)
a=dnh(root)
print("BINARY TREE DIAMETER IS : ",a.diameter)