from Tree.bst_recursive import BinarySearchTree


def findKthMax(root, k):
    if k < 1:
        return None
    node = findKthMaxRecursive(root, k)  # get the node at kth position
    if node is not None:  # check if node received
        return node.val  # return kth node value
    return None  # return None if no node found


counter = 0  # global count variable
current_max = None


def findKthMaxRecursive(root, k):
    global counter  # use global counter to track k
    global current_max  # track current max
    if root is None:  # check if root exists
        return None

    # recurse to right for max node
    node = findKthMaxRecursive(root.rightChild, k)
    if (counter is not k) and (root.val is not current_max):
        # Increment counter if kth element is not found
        counter += 1
        current_max = root.val
        node = root
    elif current_max is None:
        # Increment counter if kth element is not found
        # and there is no current_max set
        counter += 1
        current_max = root.val
        node = root
    # Base condition reached as kth largest is found
    if counter == k:
        return node  # return kth node
    else:
        # Traverse left child if kth element is not reached
        # traverse left tree for kth node
        return findKthMaxRecursive(root.leftChild, k)


BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)
BST.insert(10)

print(findKthMax(BST.root, 4))
