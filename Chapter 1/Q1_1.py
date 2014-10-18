# suppose it is an ASCII string
def is_unique(string):
    if len(string) > 256:
        return False
    else:
        isExit = [False] * 256;
        for char in string:
            if isExit[ord(char)]:   #function ord() would get the ASCII value of the char      
                return False
            else:
                isExit[ord(char)]=True
        return True



#--------------------test-------------------]
test_true = "abcdefghijklmn"
test_false = "andkgeowa"

if is_unique(test_true):
    print "test 1 passed"
else:
    print "test 1 failed"

if not is_unique(test_false):
    print "test 2 passed"
else:
    print "test 2 failed"
#--------------------test-------------------]

from random import randint

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,value):
        node = Node(value)
        #if the old list is none, set new node as the first node
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def __str__(self):
        if self.head != None:
            index = self.head
            nodestore = [str(index.value)]
            while index.next != None:
                index = index.next
                nodestore.append(str(index.value))
            return "LinkedList  [ " + "->".join(nodestore) + " ]"
        return "LinkedList  []"


    #remove the first node that have the same value as the given node_value
    def removeNode(self, node_value):
        current = self.head
        if current.value == node_value:
            self.head = self.head.next
        while(current.next != None):
            if current.next.value == node_value:
                current.next = current.next.next
                break
            else:
                current = current.next


def randomLinkedList(length, min, max):
    linkedlist = LinkedList()
    for i in range(length):
        value = randint(min, max)
        linkedlist.addNode(value)
    return linkedlist
# Q2_1.py

from classes.LinkedList import *


# use a hash table, O(n)
def deleteDups(linkedlist):
    if (linkedlist.head != None):
        currNode = linkedlist.head
        dic =  {currNode.value: True}
        while currNode.next != None:
            if currNode.next.value in dic:
                currNode.next = currNode.next.next
            else:
                dic[currNode.next.value] = True
                currNode = currNode.next


# use no data structure, O(n2)
def deleteDups2(linkedlist):
    currNode = linkedlist.head
    while currNode != None:
        runner = currNode
        while runner.next != None:
            if runner.next.value == currNode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        currNode = currNode.next




#---------------- test --------------------
L1 = randomLinkedList(9, 3, 7)
print L1
deleteDups(L1)
print L1
print
L2 = randomLinkedList(9, 3, 7)
print L2
deleteDups2(L2)
print L2
#---------------- test --------------------
# Q2_2.py
from classes.LinkedList import *


# if k = 1, return the last element
def kth_to_last(linkedlist, k):
    if k <= 0:
        return "invalid k"
    pointer2 = linkedlist.head
    for i in range(k-1):
        if pointer2.next != None:
            pointer2 = pointer2.next
        else:
            return "k exceeds the length of linkedlist"
    pointer1 = linkedlist.head
    while pointer2.next != None:
        pointer2 = pointer2.next
        pointer1 = pointer1.next
    return pointer1
   
 

#---------------test------------------
L = randomLinkedList(8, 0, 100)
print L
print "The 3th to last element is", kth_to_last(L, 3)
# Q2_3.py
from classes.LinkedList import *

def deleteNode(linkedlist, node):
    if node.next != None:
        node.value = node.next.value
        node.next = node.next.next  
    
    # if the given node is the last one, no way to delete it.
    # Here we set the last one's value to None
    else:
        node.value = None         



#-----------test--------------
L = randomLinkedList(5, 0, 100)
node = L.head.next.next         # Given access to the 3rd node
print L
print "After deleting the node"
deleteNode(L, node)
print L
# Q2_4.py
from classes.LinkedList import *

def partition(linkedlist, x):
    if linkedlist.head != None:
        p1 = linkedlist.head
        p2 = linkedlist.head.next
        while p2 != None:
            if p2.value < x:
                p1.next = p2.next
                p2.next = linkedlist.head
                linkedlist.head = p2
                p2 = p1.next
            else:
                p1 = p1.next
                p2 = p1.next



#----------------test-----------------
L = randomLinkedList(10, 0, 50)
x = 25

print L, " , x=25"   
partition(L, x)
print L 
# Q2_5.py
from classes.LinkedList import *


#The digits are stored in reverse order
def addLists_rev(L1, L2):
    p1 = L1.head
    p2 = L2.head
    carry = 0
    linkedlist_sum = LinkedList()
    while (p1 != None) or (p2 != None) or (carry != 0):
        dig_sum = carry
        if p1 != None:
            dig_sum += p1.value
            p1 = p1.next
        if p2 != None:
            dig_sum += p2.value
            p2 = p2.next
        linkedlist_sum.addNode(dig_sum%10)
        carry = dig_sum/10
    return linkedlist_sum


# The digits are stored in forward order

# Iterative implementation
def addLists_fwd(L1, L2):
    # Create two new linkedlists which are reversed version of L1 and L2
    # Use addLists_rev method, then reverse the sum list
    L1_rev = reverseLinkedlist(L1)
    L2_rev = reverseLinkedlist(L2)
    return reverseLinkedlist(addLists_rev(L1_rev, L2_rev))


# Recursive implementation of addLists_fwd
def addLists_fwd_2(L1, L2):
    # compare length of linked lists and pad the shorter one with 0
    l1_len = lengthOfLinkedlist(L1)
    l2_len = lengthOfLinkedlist(L2)
    if l1_len < l2_len:
        L1 = padInFront(L1, l2_len - l1_len)
    else:
        L2 = padInFront(L2, l1_len - l2_len)   
    # Add lists
    sumandcarry = addListsFwd2Helper(L1.head, L2.head)
    result = LinkedList()
    result.head = sumandcarry[0]   
    # If the carry is not 0, insert this at the front of the linked list 
    if sumandcarry[1] != 0:
        addNodeInFront(result, sumandcarry[1])
    return result


# Helper function for recursive adding lists
def addListsFwd2Helper(p1, p2):
    if (p1 == None) and (p2 == None):
        sumandcarry = [None,0]       # a python list stores sum node and carry
        return sumandcarry
    sumandcarry = addListsFwd2Helper(p1.next, p2.next)
    val = p1.value + p2.value + sumandcarry[1]
    dig_node = insertBefore(sumandcarry[0], val%10) 
    carry = val/10
    return [dig_node, carry]


# Helper function to insert node in the front of a linked list
def addNodeInFront(linkedlist, value):
    node = Node(value)
    node.next = linkedlist.head
    linkedlist.head = node


# Helper function to insert node before a node
def insertBefore(node, value):
    new_node = Node(value)
    new_node.next = node
    return new_node


# Helper function to create a reversed linedlist
def reverseLinkedlist(linkedlist):
    current = linkedlist.head
    newlinkedlist = LinkedList()
    while current != None:
        addNodeInFront(newlinkedlist, current.value)
        current = current.next
    return newlinkedlist


# Helper function to caculate length of a linked list
def lengthOfLinkedlist(linkedlist):
    length = 0
    current = linkedlist.head
    while current != None:
        length += 1
        current = current.next
    return length


# Helper funtion to pad the list with zeros in front
def padInFront(linkedlist, number):
    padlist = LinkedList()
    padlist.head = linkedlist.head
    for i in range(number):
        addNodeInFront(padlist, 0)
    return padlist




#----------------test--------------
L1 = randomLinkedList(3,0,9)
L2 = randomLinkedList(5,0,9)
print L1
print L2
print "In reverse order, the sum is: "
print addLists_rev(L1, L2)
print "In forward order with iterative implementation, the sum is: "
print addLists_fwd(L1, L2)
print 'In forward order with recursive implementation, the sum is: '
print addLists_fwd_2(L1, L2)
# Q2_6.py
from classes.LinkedList import *


def findBeginning(linkedlist):
    slow = linkedlist.head
    fast = linkedlist.head

    # Find meetng point
    while (fast != None) and (fast.next != None):
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    
    # Check whether it is a circular linked list
    if fast == None or fast.next == None:
        return None

    # Move one runner to head. Making them move at same pace, they will meet at the beginning of the loop
    fast = linkedlist.head
    while fast != slow:
        slow = slow.next
        fast = fast.next

    return fast



# -----------------test------------------
nodes_number = 100
nodes_in_loop = 20
L = LinkedList()
current = L.head
store = []                  # store nodes to help creating loop

# Create a linked list
for i in range(nodes_number):
    L.addNode(i)
    current = L.head if i==0 else current.next
    store.append(current)

# Creat loop
current.next = None if nodes_in_loop <= 0 else store[nodes_number - nodes_in_loop]

beginning = findBeginning(L)
print beginning              # 80
# Q2_7.py
from classes.LinkedList import *

# Iterative approch
def isPalindrome_iter(linkedlist):
    if linkedlist.head == None:
        return None
    fast = linkedlist.head
    slow = linkedlist.head
    firsthalf = []
    while fast != None and fast.next != None:
        firsthalf.append(slow.value)
        slow = slow.next
        fast = fast.next.next
    if fast != None:
        slow = slow.next
    while slow != None:
        if firsthalf.pop() != slow.value:
            return False
        else:
            slow = slow.next
    return True


# Recursive approch
def isPalindrome_recu(linkedlist):
    length = lengthOfLinkedlist(linkedlist)
    current = linkedlist.head
    result = isPalindrome_recu_helper(current, length)
    return result[1]



def isPalindrome_recu_helper(current, length):
    if current == None:
        return [None, True]             
    elif length == 1:
        return [current.next, True]
    elif length == 2:
        return [current.next.next, current.value == current.next.value]
    
    # result is a python list stores two variables 
    result = isPalindrome_recu_helper(current.next, length - 2)

    if (result[0] == None) or (not result[1]):
        return result
    else:
        result[1] = current.value == result[0].value
        result[0] = result[0].next
        return result


def lengthOfLinkedlist(linkedlist):
    length = 0
    current = linkedlist.head
    while current != None:
        length += 1
        current = current.next
    return length



# -------------------test------------------
L1 = randomLinkedList(3, 3, 4)
print "L2:", L1
print "isPalindrome_iter: ", isPalindrome_iter(L1)
print "isPalindrome_recu: ", isPalindrome_recu(L1)
L2 = LinkedList()
for i in range(1,4):
    L2.addNode(i)
for i in range(3, 0, -1):
    L2.addNode(i)
print "L3:", L2
print "isPalindrome_iter: ", isPalindrome_iter(L2)
print "isPalindrome_recu: ", isPalindrome_recu(L2)
# Q3_1.py
# Fixed division
class SingleArrayStacks(object):

    def __init__(self, stacksize = 100, number = 3):
        self.stacksize = stacksize
        self.number = number
        self.array = [None] * self.stacksize * self.number
        self.pointer = [-1] * self.number

    def push(self, stacknum, value):
        if self.pointer[stacknum] + 1 >= self.stacksize:
            print "Out of space"
        else:
            self.pointer[stacknum] += 1
            self.array[self.stacktop(stacknum)] = value

    def pop(self, stacknum):
        if self.pointer[stacknum] < 0:
            return "Trying to pop an empty stack."
        else:
            data = self.array[self.stacktop(stacknum)]
            self.array[self.stacktop(stacknum)] = None
            self.pointer[stacknum] -= 1
            return data

    def peek(self, stacknum):
        if self.pointer[stacknum] < 0:
            print "Empty stack"
        else:
            return self.array[self.stacktop(stacknum)]

    def isEmpty(self, stacknum):
        return self.pointer[stacknum] == -1

    def stacktop(self, stacknum):
        return self.stacksize * stacknum + self.pointer[stacknum]



#-----------------test-----------------
if __name__ == "__main__":
    array = SingleArrayStacks()
    array.push(2, 11)
    array.push(2, 13)
    print array.pop(0)  # Trying to pop an empty stack.
    print array.peek(2) # 13
    array.push(0, 20)
    array.push(0, 30)
    print array.pop(0)  # 30
    print array.peek(0) # 20
    
# Q3_2.py
class StackWithMin:
    
    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, value):
        self.stack.append(value)
        if len(self.min) == 0 or value <= self.min[-1]:
            self.min.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return None
        data = self.stack.pop()
        if data == self.min[-1]:
            self.min.pop()
        return data

    def getMin(self):
        if len(self.min)==0:
            return None
        return self.min[-1]


#--------------test-----------------
from random import randrange
Stack = StackWithMin()
for i in range(15):
    data = randrange(1,100)
    Stack.push(data)
    print data,
print ""

for i in range(15):
    print "Poped", Stack.pop(), " New min", Stack.getMin()
# Q3_3.py
class SetOfStacks:
    
    def __init__(self,capacity):
        self.capacity = capacity
        self.stacks = []

    def push(self, value):
        if (len(self.stacks) == 0) or (len(self.stacks[-1]) == self.capacity):
            self.stacks.append([])
        self.stacks[-1].append(value)

    def pop(self):
        if len(self.stacks) == 0:
            return None
        data = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return data
    
    # Pop operation on a specifit sub-stack. (Index begins with 1)
    # Not "rolling over" version. OK with some stacks not at full capacity
    def popAt(self, index):
        if index < 1 or index > len(self.stacks) or len(self.stacks[index-1]) == 0:
            return None
        else:
            return self.stacks[index-1].pop() 



#-----------------test-------------------
def test():
    setofstacks = SetOfStacks(8)
    for i in range(24):
        setofstacks.push(i)
        print i,
    print ""

    for i in range(5):
        print "Poped", setofstacks.pop()

    print "Test for popAt"
    for i in range(5):
        for i in range(3):
            print "Poped", setofstacks.popAt(i+1)


if __name__ == "__main__":
    test()
# Q3_4.py    
class Hanoi:
    
    def __init__(self, size):
        self.towers = [[], [], []]
        self.size = size
        self.towers[0] = [x for x in range(size, 0, -1)]

    def playHanoi(self):
        self.printTowers()
        self.moveDisk(self.size, 1, 2, 3)
        self.printTowers()

    def moveDisk(self, size, fr, helper, to):
        if size == 1:
            data = self.towers[fr-1].pop()
            self.towers[to-1].append(data)
            print "Disk", data, ": Tower", fr, "->", to      
        else:
            self.moveDisk(size - 1, fr, to, helper)
            self.moveDisk(1, fr, helper, to)
            self.moveDisk(size - 1, helper, fr, to)

    def printTowers(self):
        for i in self.towers:
            print i




#----------------test---------------
hanoi = Hanoi(4)
hanoi.playHanoi()
# Q3_5.py
""" Implement a Queue class using two stacks."""

class MyQueue:

    def __init__(self):
        self.stackOldest = Stack()
        self.stackNewest = Stack()

    def push(self, value):
        self.stackNewest.push(value)

    def pop(self):
        if len(self.stackOldest.stack) == 0:
            self.moveToOldest()
        return self.stackOldest.pop()
    
    def peek(self):
        if len(self.stackOldest.stack) == 0:
            self.moveToOldest()
        return self.stackOldest.peek()

    def moveToOldest(self):
        while len(self.stackNewest.stack):
            self.stackOldest.push(self.stackNewest.pop())

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return None if len(self.stack) == 0 else self.stack.pop()

    def peek(self):
        return None if len(self.stack) == 0 else self.stack[-1]



#----------------test-------------------
if __name__ == "__main__":
    queue = MyQueue()
    for i in range(1,5):
        queue.push(i)
        print "Enqueued",i
        queue.push(i*2)
        print "Enqueued", i*2
        data = queue.pop()
        print "Dequeued", data
# Q3_6.py
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return None if self.isEmpty() else self.stack.pop()

    def peek(self):
        return None if self.isEmpty() else self.stack[-1]


    def isEmpty(self):
        return len(self.stack) == 0


# Sort stack without using other data structure except Stack
def sortStack(s):
    sortedStack = Stack()
    while not s.isEmpty():
        data = s.pop()      
        while (not sortedStack.isEmpty()) and sortedStack.peek() > data:
            stack.push(sortedStack.pop())
        sortedStack.push(data)
    return sortedStack



#---------------test---------------
if __name__ == '__main__':
    from random import randrange
    stack = Stack()
    for i in range(10):
        stack.push(randrange(0,100))
    print "Before sorting",stack.stack
    print "After sorting ", sortStack(stack).stack
# Q3_7.py
from collections import deque

# Using a deque datatype as an implementation of queue

class Animal(object):

    def __init__(self, name):
        self.name = name
        self.order = -1

    def __str__(self):
        return "Animal: " + self.name


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def __str__(self):
        return "Cat: " + self.name

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def __str__(self):
        return "Dog: " + self.name



class AnimalQueue(object):
    
    def __init__(self):
        self.Dog = deque()
        self.Cat = deque()
        self.order = 0

    def enqueue(self, animal):
        animal.order = self.order
        self.order += 1 
        if isinstance(animal, Cat):
            self.Cat.append(animal)
        else:
            self.Dog.append(animal)

    def dequeueAny(self):
        if len(self.Dog) == 0:
            return self.dequeueCat()
        if len(self.Cat) == 0:
            return self.dequeueDog()
        if self.Dog[0].order < self.Cat[0].order:
            return self.Dog.popleft()
        else:
            return self.Cat.popleft()

    def dequeueDog(self):
        return self.Dog.popleft() if len(self.Dog) != 0 else None


    def dequeueCat(self):
        return self.Cat.popleft() if len(self.Cat) != 0 else None



#------------------test--------------------
if __name__ == "__main__":
    animals = AnimalQueue()
    animals.enqueue(Cat("cat_1"))
    animals.enqueue(Cat("cat_2"))
    animals.enqueue(Cat("cat_3"))
    animals.enqueue(Dog("dog_1"))
    animals.enqueue(Cat("cat_4"))
    animals.enqueue(Dog("dog_2"))
    print animals.dequeueAny()      # Cat: cat_1
    print animals.dequeueDog()      # Dog: dog_1
    print animals.dequeueCat()      # Cat: cat_2
    for i in range(3):
        print animals.dequeueAny()  # Cat: cat_3
                                    # Cat: cat_4
                                    # Dog: dog_2
    print animals.dequeueAny()      # None
