class BinaryTree(object):

    def __init__(self, rootobj):
        self.key = rootobj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.leftChild
            self.rightChild = t

    def getLeftchild(self):
        return self.leftChild

    def getRightchild(self):
        return self.rightChild

    def getRootVal(self):
        return self.key

    def setRootVal(self, obj):
        self.key = obj


r = BinaryTree('a')
r.insertLeft('b')
r.insertRight('c')


def postorder(tree):
    if tree is not None:
        postorder(tree.getLeftchild())
        postorder(tree.getRightchild())
        print(tree.getRootVal)


print(postorder(r))
