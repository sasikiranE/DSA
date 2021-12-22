class Node:

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
            return
        curr = self.root
        while True:
            if data < curr.data:
                if curr.left is None:
                    curr.left = newNode
                    return
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = newNode
                    return
                curr = curr.right
    
    # Depth First Traversals.
    def preorder(self):
        self.__preorder(self.root)
        print()

    def __preorder(self, root):
        if root is None:
            return
        print(root.data, end=' ')
        self.__preorder(root.left)
        self.__preorder(root.right)
    
    def inorder(self):
        self.__inorder(self.root)
        print()

    def __inorder(self, root):
        if root is None:
            return
        self.__inorder(root.left)
        print(root.data, end=' ')
        self.__inorder(root.right)

    def postorder(self):
        self.__postorder(self.root)
        print()

    def __postorder(self, root):
        if root is None:
            return
        self.__postorder(root.left)
        self.__postorder(root.right)
        print(root.data, end=' ')

    def find(self, target):
        curr = self.root

        while curr is not None:
            if target < curr.data:
                curr = curr.left
            elif target > curr.data:
                curr = curr.right
            else:
                return True
        return False

    def height(self):
        return self.__height(self.root)

    def __height(self, root):
        if root is None:
            return -1
        if root.left is None and root.right is None:
            return 0
        return 1 + max(self.__height(root.left), self.__height(root.right))

    def getMin(self):
        if self.root is None:
            raise Exception("Cannot get mininum value. Tree is empty!")
        curr = self.root
        while curr.left is not None:
            curr = curr.left
        return curr.data

    def getMax(self):
        if self.root is None:
            raise Exception("Cannot get maximum value. Tree is empty!")
        curr = self.root
        while curr.right is not None:
            curr = curr.right
        return curr.data

    def equals(self, other):
        return self.__equals(self.root, other.root)

    def __equals(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        
        if root1 is not None and root2 is not None:
            return root1.data == root2.data and self.__equals(root1.left, root2.left) and self.__equals(root1.right, root2.right)
        
        return False

    def isBinarySearchTree(self):
        inf = 1e9 + 7
        return self.__isBST(self.root, -inf, inf)

    def __isBST(self, root, low, high):
        if root is None:
            return True
        if root.data < low or root.data > high:
            return False
        return self.__isBST(root.left, low, root.data - 1) and self.__isBST(root.right, root.data + 1, high)

