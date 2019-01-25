class Node:
    def __init__(self, newValue):
        self.value = newValue
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.firstnode = None

    def append(self, input):

        temp = self.firstnode

        if temp is None:

            newNode = Node(input)
            temp = newNode
            print(temp.value)

            return temp.value


        else:

            if temp.value > self.firstnode:
                temp = temp.left
                bst.append(input)



            else:
                temp = temp.right
                bst.append(input)

    def preOrder(self):

        temp = self.firstnode

        while temp is not None:
            preOrder(temp.right)
            preOrder(temp.left)

            print(temp)


bst = BST()
bst.append(9)
bst.append(2)
bst.append(10)
bst.append(8)
bst.append(5)