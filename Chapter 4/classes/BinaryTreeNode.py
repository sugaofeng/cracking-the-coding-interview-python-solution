class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def setLeft(self, leftvalue):
        leftnode = BinaryTreeNode(leftvalue)
        self.left = leftnode
        if leftnode != None:
            leftnode.parent = self

    def setRight(self, rightvalue):
        rightnode = BinaryTreeNode(rightvalue)
        self.right = rightnode
        if rightnode != None:
            rightnode.parent = self

class BTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def setLeftChild(self, leftnode):
        self.left = leftnode
        if leftnode != None:
            leftnode.parent = self

    def setRightChild(self, rightnode):
        self.right = rightnode
        if rightnode != None:
            rightnode.parent = self


#4.1
# O(n^2) Naive algorithms
def isBalanced(root):
    if root == None:
        return True
    heightDiff = getHeight(root.left) - getHeight(root.right)
    if abs(heightDiff) > 1:
        return False
    return isBalanced(root.left) and isBalanced(root.right)

def getHeight(root):
    if root == None:
        return 0
    return max(getHeight(root.left), getHeight(root.right)) + 1



# Another implementation with O(n) 
def isBalanced_2(root):
    return checkHeight(root)[0]

def checkHeight(root):
    if root == None:
        return True, 0
    isLeftBalanced, leftHeight = checkHeight(root.left)
    isRightBalanced, rightHeight = checkHeight(root.right)
    heightDiff = leftHeight - rightHeight
    treeHeight = max(leftHeight, rightHeight) + 1
    return abs(heightDiff) <= 1 and isLeftBalanced and isRightBalanced, treeHeight



#-------------------test-----------------
if __name__ == "__main__":
    btree = BTreeNode(1)
    btree.setLeftChild(BTreeNode(2))
    btree.setRightChild(BTreeNode(3))
    btree.right.setLeftChild(BTreeNode(4))
    btree.right.left.setLeftChild(BTreeNode(5))
    print isBalanced(btree)                     # False
    print isBalanced_2(btree)                   # False
#4.2
# Given a directed graph, find out whether there is a route between two nodes
# Dictionary is used here to store graphc
# Each key is a node, and value for the key is a python list storing adjacent nodes

from collections import deque

# Using BFS
def hasRoute1(G, begin, end):
    visited = {}
    queue = deque()
    if begin != None:
        queue.append(begin)
    while len(queue) != 0:
        node = queue.popleft()
        if node == end:
            return True
        if node not in visited:
            visited[node] = True
        for nd in G.get(node, []):
            queue.append(nd)
    return False


# Using DFS
def hasRoute2(G, begin, end, visited = None):
    if visited == None:
        visited = {}
    if begin == end:
        return True
    visited[begin] = True
    for node in G.get(begin,[]):
        if node not in visited:
            if hasRoute2(G, node, end, visited):
                return True
    return False



# --------------test----------------
if __name__ == "__main__":
    G = dict()
    G[1]=[6,2,3]
    G[2]=[4,3]
    G[3]=[5]
    G[4]=[6,5]
    print hasRoute1(G, 4, 1)
    print hasRoute1(G, 1, 4)
    print hasRoute2(G, 1, 4)
    print hasRoute2(G, 4, 1)
    print hasRoute1(G, 1, 7)
    print hasRoute2(G, 8, 1)
#4.3
class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def setLeftChild(self, leftvalue):
        leftnode = TreeNode(leftvalue)
        self.left = leftnode
        if leftnode != None:
            leftnode.parent = self

    def setRightChild(self, rightvalue):
        rightnode = TreeNode(rightvalue)
        self.right = rightnode
        if rightnode != None:
            rightnode.parent = self

# print order: middle left right
def printTree(tree):
    if tree != None: 
        print tree.value
        print tree.value, "left:",
        printTree(tree.left)
        print ""
        print tree.value, "right:",
        printTree(tree.right)   



def arrayToBST(array, start, end):
    if start > end:
        return None
    middle = (start + end)/2 
    tree = TreeNode(array[middle])
    tree.left = arrayToBST(array, start, middle-1)
    tree.right = arrayToBST(array, middle+1, end)
    return tree


# --------------test--------------
if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5, 6]
    tree = arrayToBST(array, 0, len(array)-1)
    printTree(tree)
#4.4
from classes.BinaryTreeNode import *

class LinkedListNode:
	
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None

	def addNode(self, value):
		node = LinkedListNode(value)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node



# Using breadth first search
def createLevelLinkedlist1(root):
	result = []
	parents = LinkedList()
	if root is not None:
		parents.addNode(root)
	while parents.head is not None:
		result.append(parents)
		children = LinkedList()
		current = parents.head
		while current is not None:	
			if current.value.left is not None:
				children.addNode(current.value.left)
			if current.value.right is not None:
				children.addNode(current.value.right)
			current = current.next
		parents = children
	return result


	
# Using deep first search
def createLevelLinkedlist2(root, result = None, deep = 0):
	if result is None:
		result = []
	if root is None:
		return result
	if deep == len(result):
		L = LinkedList()
		result.append(L)
	result[deep].addNode(root)
	createLevelLinkedlist2(root.left, result, deep+1)
	createLevelLinkedlist2(root.right, result, deep+1)
	return result



# ------------------test---------------------------
# A binary search tree
#     5
#    / \
#   3   6
#  / \   \
# 1   4   8
#  \
#   2

def test():
	# create a tree
	bstree = BinaryTreeNode(5)
	bstree.setLeft(3)
	bstree.left.setLeft(1)
	bstree.left.left.setRight(2)
	bstree.left.setRight(4)
	bstree.setRight(6)
	bstree.right.setRight(8)
    
    # create a list of linkedlists containing tree nodes in each level
	result1 = createLevelLinkedlist1(bstree)
	result2 = createLevelLinkedlist2(bstree)
	
	print "Test for method 1:"
	printTnodeLinkedlistArray(result1)
	print "Test for method 2:"
	printTnodeLinkedlistArray(result2)


def printTnodeLinkedlistArray(resultlist):
	for i, llist in enumerate(resultlist):
		print i, "level:",
		p = llist.head
		while p is not None:
			print p.value.value,
			p = p.next
		print ""


if __name__ == "__main__":
	test()
#4.5
from classes.BinaryTreeNode import *
import sys


# In-order traversal, and compare an element to the previous one
def isBST1(btree):
    return checkBST1(btree)[0]

def checkBST1(btree, previous = -sys.maxint-1):
    if btree is None or btree.value is None:
        return True, previous    
    
    [isleftbst, previous] = checkBST1(btree.left, previous)
    if not isleftbst:
        return False, previous
    
    if btree.value < previous:
        return False, previous
    previous = btree.value

    if not checkBST1(btree.right, previous)[0]:
        return False, previous

    return True, previous


# Passing down min and max values to check the node value is within the range
def isBST2(btree, minvalue = -sys.maxint-1, maxvalue = sys.maxint):
    if btree is None or btree.value is None:
        return True

    if btree.value < minvalue or btree.value > maxvalue:
        return False

    if (not isBST2(btree.left, minvalue, btree.value)) \
        or (not isBST2(btree.right, btree.value, maxvalue)):
        return False

    return True



# ----------------test------------------
#           5
#          / \
#         3   9
#        / \ / \
#       1  4 7 10

def test():
    btree = BinaryTreeNode(5)
    btree.setLeft(3)
    btree.setRight(9)
    btree.left.setLeft(1)
    btree.left.setRight(4)
    btree.right.setLeft(7)
    btree.right.setRight(10)

    print isBST1(btree)         # True
    print isBST2(btree)         # True



if __name__ == "__main__":
    test()
#4.6

from classes.BinaryTreeNode import *


def findNextNode(node):
    if node is None:
        return None

    # Find the leftmost node of right subtree    
    if node.right is not None:
        return findLeftMost(node.right)

    # Go up until the node is on left substree of that parent
    else:
        return findParentToWhomeIsLeft(node)


def findLeftMost(node):
    current = node
    while current.left is not None:
        current = node.left
    return current

def findParentToWhomeIsLeft(node):
    current = node
    parent = current.parent
    while parent is not None and parent.left is not current:
        parent = parent.parent
        current = current.parent
    return parent



# ----------------test------------------
#           5
#          / \
#         3   7
#        / \   \
#       1   4   8
#      /
#     0
#
# In-order traversal: 0 1 3 4 5 7 8

def test():
    n5 = BinaryTreeNode(5)
    n5.setLeft(3)
    n3 = n5.left
    n5.setRight(7)
    n7 = n5.right
    n3.setLeft(1)
    n1 = n3.left
    n3.setRight(4)
    n4 = n3.right  
    n7.setRight(8)
    n8 = n7.right
    n1.setLeft(0)
    n0 = n1.left
        
    for node in [n5, n3, n7, n1, n4, n8, n0]:
        next = findNextNode(node)
        print node.value, "next:", next.value if next is not None else next


if __name__ == "__main__":
    test()

#4.7

from classes.BinaryTreeNode import *


# Mehod 1: if nodes have links to parents, Go up levels to see whether 
# a node's ancestor is another node's ancestor
def commonAncestor_1(p, q):
    if p is None:
        return None
    if cover(p, q):
        return p
    current = p
    parent = current.parent
    while parent is not None:
        if (parent is q) or (parent.left is current and cover(parent.right, q))\
           or (parent.right is current and cover(parent.left, q)):
            return parent
        current = parent
        parent = parent.parent
    return None

# check if n is a descendent of root
def cover(root, n):
    if root is None:
        return False
    if root is n:
        return True
    return cover(root.left, n) or cover(root.right, n)



# Method 2: if nodes have no links to parents.
def commonAncestor_2(root, p, q):
    result = commonAncestor2_helper(root, p, q)
    if result[1]:
        return result[0]
    return None

def commonAncestor2_helper(root, p, q):
    if root is None:
        return None, False
    if root is p and root is q:
        return root, True
    
    left = commonAncestor2_helper(root.left, p, q)
    if left[1] == True:     # Already found ancestor in the subtree
        return left
    
    right = commonAncestor2_helper(root.right, p, q)
    if right[1] == True:    # Already found ancestor in the subtree
        return right
    
    # If One of subtree return p and one of subtree return q, found common ancestor
    if left[0] != None and right[0] != None:
        return root, True
    
    # If root is p or q and one of the subtrees contain q or p, the root is common ancestor
    # If no p or q in the subtree, return root, False
    elif root is p or root is q:
        isAncestor = True if left[0] != None or right[0] != None else False
        return root, isAncestor
    
    # The rest condition:
    # 1) One of the subtree contains only p or q, another subtree is None, return p or q, False
    # 2) None of subtrees contain p or q, return None, False
    else:
        return left[0] if left[0] != None else right[0], False




# ------------------test--------------------
#             10
#            /  \
#           5    6
#          / \  / \
#         1  2  3  4
#           /
#          7

def test():
    root = BinaryTreeNode(10)
    root.setLeft(5)
    root.setRight(6)
    root.left.setLeft(1)
    root.left.setRight(2)
    root.right.setLeft(3)
    root.right.setRight(4)
    root.left.right.setLeft(7)

    # test case 1: node 7 and 6  --> Common ancestor: 10
    # test case 2: node 2 and 5 --> Common ancestor: 5
    # test case 3: node 6 and a node not in the tree  --> Common ancestor: None 
    tests = [(root.left.right.left, root.right), (root.left.right, root.left), (root.right, BinaryTreeNode(9))]
    methods = [commonAncestor_1, commonAncestor_2] 
    for test in tests:
        for method in methods:
            if method == commonAncestor_1:
                ancestor = method(test[0], test[1])
            else:
                ancestor = method(root, test[0], test[1])
            print ancestor.value if ancestor is not None else None
             

if __name__ == "__main__":
    test()
#4.8

from classes.BinaryTreeNode import *
from collections import deque

# Create an algorithm to decide if T2 is a subtree of T1

def containTree(T1, T2):
    if T2 is None:
        return True
    queue = deque()
    if T1 is not None:
        queue.append(T1)
    while len(queue) != 0:
        node = queue.popleft()
        if node.value == T2.value:
            if matchTree(node, T2):
                return True
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return False


def matchTree(n1, n2):
    if n1 == None and n2 == None:
        return True
    if n1 == None or n2 == None:
        return False
    if n1.value != n2.value:
        return False
    return matchTree(n1.left, n2.left) and matchTree(n1.right, n2.right)






# ----------------test-----------------
# T1          1            T2        2
#            / \                    / \
#           2   3                  4   2
#          / \   \                    / 
#         4   2   2                  8   
#            / 
#           8   
#               
              

def main():
    T1 = BinaryTreeNode(1)
    T1.setLeft(2)
    T1.setRight(3)
    T1.left.setLeft(4)
    T1.left.setRight(2)
    T1.right.setRight(2)
    T1.left.right.setLeft(8)
    T2 = BinaryTreeNode(2)
    T2.setLeft(4)
    T2.setRight(2)
    T2.right.setLeft(8)

    print containTree(T1, None)          # True
    print containTree(None, T2)          # False
    print containTree(T1, T2)            # True
    print containTree(T1, BinaryTreeNode(4))    # True


if __name__ == "__main__":
    main()
    
#4.9

from classes.BinaryTreeNode import *

def findSum(node, givenSum, path=None, depth=0):
    if node is None:
        return
    if path is None:
        path = []
    if len(path) > depth:
        path[depth] = node.value
    else:
        path.append(node.value)
    
    # Look up to see if there are paths end up with this node and sum to the given value
    temp = 0
    for i in range(depth, -1, -1):
        temp += path[i]
        if temp == givenSum:
            printPath(path, i, depth)
    
    findSum(node.left, givenSum, path, depth+1)
    findSum(node.right, givenSum, path, depth+1)


def printPath(path, start, end):
    for i in range(start, end + 1):
        print path[i],
    print ""



# --------------test----------------
#               1
#              / \
#             2   3
#            / \ / \
#           4  5 3  4 
#             /
#            7
# Sum = 7
# Path:
# 1 2 4
# 2 5
# 7
# 1 3 3
# 3 4

def main():
    givenSum = 7
    root = BinaryTreeNode(1)
    root.setLeft(2)
    root.setRight(3)
    root.left.setLeft(4)
    root.left.setRight(5)
    root.right.setLeft(3)
    root.right.setRight(4)
    root.left.right.setLeft(7)

    findSum(root, givenSum)


if __name__ == "__main__":
    main()
