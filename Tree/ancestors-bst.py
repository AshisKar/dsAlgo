from Tree.bst_recursive import BinarySearchTree


# my solution
# def findAncestors(root, k):
#     # Write your code here
#
#     lis = findAncestors_rec(root, k, [])
#     return lis
#
#
# def findAncestors_rec(root, k, ancestors):
#     if root.val < k:
#         ancestors.append(root.val)
#         return findAncestors_rec(root.rightChild, k, ancestors)
#     elif root.val > k:
#         ancestors.append(root.val)
#         return findAncestors_rec(root.leftChild, k, ancestors)
#     else:
#         if len(ancestors) == 0:
#             ancestors.append(root.val)
#         return ancestors

# iterative
def findAncestors(root, k):
    if not root:  # check if root exists
        return None
    ancestors = []  # empty list of ancestors
    current = root  # iterator current set to root

    while current is not None:  # iterate until we reach None
        if k > current.val:  # go right
            ancestors.append(current.val)
            current = current.rightChild
        elif k < current.val:  # go left
            ancestors.append(current.val)
            current = current.leftChild
        else:  # when k == current.val
            return ancestors[::-1]
    return []

# recursive
# def findAncestors(root, k):
#     result = []
#     recfindAncestors(root, k, result)  # recursively find ancestors
#     return str(result)  # return a string of ancestors
#
#
# def recfindAncestors(root, k, result):
#     if root is None:  # check if root exists
#         return False
#     elif root.val is k:  # check if val is k
#         return True
#     recur_left = recfindAncestors(root.leftChild, k, result)
#     recur_right = recfindAncestors(root.rightChild, k, result)
#     if recur_left or recur_right:
#         # if recursive find in either left or right sub tree
#         # append root value and return true
#         result.append(root.val)
#         return True
#     return False  # return false if all failed


BST = BinarySearchTree(6)
BST.insert(1)
BST.insert(133)
BST.insert(12)
print(findAncestors(BST.root, 12))

BST = BinarySearchTree(6)
BST.insert(1)
BST.insert(133)
BST.insert(12)
print(findAncestors(BST.root, 12))
