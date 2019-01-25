class Node:
    def __init__(self, newValue):
        self.value = newValue
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.rootnode = None
#
#     # two appends so that I can return self.rootnode=node without
#     # pointing self.rootnode to something else and then it is easier to recursivly
#     # call stuff
#
    def append(self, input, node = None):
        temp = self.rootnode
        if temp is None:
            newNode = Node(input)
            self.rootnode = newNode
            return
        if node is None:
            self.append(input, self.rootnode)
            return
        if node.value > input:  # left hand side
            if (node.left is None):
                newNode = Node(input)
                node.left = newNode
            else:
                self.append(input, node.left)  # recursive part=
        elif node.value < input:  # righthandside
            if (node.right is None):
                newNode = Node(input)
                node.right = newNode
            else:
                self.append(input, node.right)  # recursive part=
        else:
            print("The number already exists in the tree")


    def preOrder(self, node = None):
        if node is None:
            self.preOrder(self.rootnode)
            return
        print(node.value)
        if node.left is not None:
            self.preOrder(node.left)
        if node.right is not None:
            self.preOrder(node.right)

    def inOrder(self, node = None):
        if node is None:
            self.inOrder(self.rootnode)
            return
        if node.left is not None:
            self.inOrder(node.left)
        print(node.value)
        if node.right is not None:
            self.inOrder(node.right)

    def postOrder(self, node = None):
        if node is None:
            self.postOrder(self.rootnode)
            return
        if node.left is not None:
            self.postOrder(node.left)
        if node.right is not None:
            self.postOrder(node.right)
        print(node.value)


bst = BST()
bst.append(7)
bst.append(2)
bst.append(6)
bst.append(9)
bst.append(8)
bst.append(11)

bst.preOrder()
print()
bst.inOrder()
print()
bst.postOrder()