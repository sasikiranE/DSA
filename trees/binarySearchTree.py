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

