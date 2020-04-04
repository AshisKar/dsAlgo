class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, val):
        if self is None:
            self = Node(val)
            return
        current = self
        while current:
            parent = current
            if val < current.val:
                current = current.leftChild
            else:
                current = current.rightChild

        if val < parent.val:
            parent.leftChild = Node(val)
        else:
            parent.rightChild = Node(val)

    def search(self, val):
        if self is None:
            return self
        current = self
        while current and current.val != val:
            if val < current.val:
                current = current.leftChild
            else:
                current = current.rightChild
        return current

    def copy(self, node2):  # When `self` needs to be modified
        self.val = node2.val
        if node2.leftChild:
            self.leftChild = node2.leftChild
        if node2.rightChild:
            self.rightChild = node2.rightChild

    def delete(self, val):
        # case 1: Tree is empty
        if self is None:
            return False

        # Searching for the given value
        node = self
        while node and node.val != val:
            parent = node
            if val < node.val:
                node = node.leftChild
            else:
                node = node.rightChild

        # case 2: If data is not found
        if node is None or node.val != val:
            return False

            # case 3: leaf node
        elif node.leftChild is None and node.rightChild is None:
            if val < parent.value:
                parent.leftChild = None
            else:
                parent.rightChild = None
            return True

            # case 4: node has left child only
        elif node.leftChild and node.rightChild is None:
            if parent is None:  # When node is root
                '''
                Have to create a deepcopy because 'self' is a local variable
                and changing it will not overwrite 'root' in the
                binarySearchTree class
                '''
                self.copy(self.leftChild)
                self.leftChild = None  # Setting the leftChild to `None`
            elif val < parent.val:
                parent.leftChild = node.leftChild
            else:
                parent.rightChild = node.leftChild
            return True

            # case 5: node has right child only
        elif node.rightChild and node.leftChild is None:
            if parent is None:  # When node is root
                '''
                Have to create a deepcopy because 'self' is a local variable
                and changing it will not overwrite 'root' in the
                binarySearchTree class
                '''
                self.copy(self.rightChild)
                self.rightChild = None  # Setting the leftChild to `None`
            elif val < parent.val:
                parent.leftChild = node.rightChild
            else:
                parent.rightChild = node.rightChild
            return True

        # case 6: node has two children
        else:
            replaceNodeParent = node
            replaceNode = node.rightChild
            while replaceNode.leftChild:
                replaceNodeParent = replaceNode
                replaceNode = replaceNode.leftChild

            node.val = replaceNode.val
            if replaceNode.rightChild:
                if replaceNodeParent.val > replaceNode.val:
                    replaceNodeParent.leftChild = replaceNode.rightChild
            elif replaceNodeParent.val < replaceNode.val:
                replaceNodeParent.rightChild = replaceNode.rightChild
            else:
                if replaceNode.val < replaceNodeParent.val:
                    replaceNodeParent.leftChild = None
                else:
                    replaceNodeParent.rightChild = None


class BinarySearchTree:
    def __init__(self, val):
        self.root = Node(val)

    def setRoot(self, val):
        self.root = Node(val)

    def getRoot(self):
        return self.root.get()

    def insert(self, val):
        self.root.insert(val)

    def search(self, val):
        return self.root.search(val)
