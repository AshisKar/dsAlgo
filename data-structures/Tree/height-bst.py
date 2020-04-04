from Tree.bst_recursive import BinarySearchTree


def findHeight(root):
    if root is None:  # check if root exists
        return -1  # no root means -1 height
    else:
        max_sub_tree_height = max(
            findHeight(root.leftChild),
            findHeight(root.rightChild)
        )  # find the max height of the two sub-tree
        # add 1 to max height and return
        return 1 + max_sub_tree_height


BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)
BST.insert(12)
BST.insert(10)
BST.insert(14)


print(findHeight(BST.root))