class Node:
    def __init__(self, newValue, newNext):
        self.value = newValue
        self.next = newNext


class LinkedList:
    def __init__(self):
        self.firstnode = None

    def append(self, input):
        if self.firstnode is None:
            newNode = Node(input, None)
            self.firstnode = newNode
            return
        temp = self.firstnode
        while (temp.next is not None):
            temp = temp.next
        temp.next = Node(input, None)
        return

    def remove(self, input):
        if (self.firstnode is None):
            print("There's nothing in the list to get rid off")
            return
        temp = self.firstnode
        if (temp.value == input):
            self.firstnode = temp.next
            return
        while (temp.next is not None):
            if (temp.next.value != input):
                temp = temp.next
            else:  # Deleting the node
                temp.next = temp.next.next
                return
        print("This value doesn't exist")
        return

    def traversal(self):
        temp = self.firstnode
        while (temp is not None):
            print(temp.value)
            temp = temp.next

    def isEmpty(self):
        if self.firstnode is None:
            return True
        return False

    def search(self, input):
        temp = self.firstnode
        while (temp is not None):
            if (temp.value != input):
                temp = temp.next
            else:
                return True
        else:
            return False

    def length(self):  # works
        numberOfItems = 0
        if self.firstnode is None:
            print("There is nothing in the list")
        temp = self.firstnode
        while (temp is not None):
            temp = temp.next
            numberOfItems += 1
        return numberOfItems

    def index(self, input):  # works
        position = 1
        if self.firstnode is None:
            print("there is nothing in the list")
            return

        temp = self.firstnode

        while (input != temp.value):
            temp = temp.next
            position = position + 1
        else:

            return position

    def insert(self, pos, input):
        counter = 0
        if self.firstnode is None:
            newNode = Node(input, None)
            self.firstnode = newNode
            return

        temp = self.firstnode

        if pos == 0:
            newNode = Node(input, temp)
            self.firstnode = newNode
            return

        while (counter != pos - 1 and temp is not None):
            counter = counter + 1
            temp = temp.next

        if counter == pos - 1:
            newNode = Node(input, temp.next)
            temp.next = newNode
            return
        else:
            print("Your position goes beyond the end of the list")

    def pop(self):  # works
        if self.firstnode is None:
            print("There's nothing in the list")
            return
        temp = self.firstnode
        if temp.next is None:
            result = temp.value
            self.firstnode = None
            return result
        while (temp.next.next is not None):
            temp = temp.next
        else:
            result = temp.next.value
            temp.next = temp.next.next
            return result

    def poppos(self, input):  # works
        counter = 1
        if self.firstnode is None:
            print("There's nothing in the list")
            return
        temp = self.firstnode
        if input == 0:
            self.firstnode = temp.next
            return
        while counter != input:
            counter = counter + 1
            temp = temp.next
        else:
            temp.next = temp.next.next
            return temp.next.value

    def get_value(self, pos):
        temp = self.firstnode
        for x in range(0, pos):
            if (temp is None):
                print("You are going beyond the end of the list.")
                return
            temp = temp.next
        else:
            return temp.value


class Stack:
    def __init__(self):
        self.linkedlist = LinkedList()

    def push(self, input):
        self.linkedlist.append(input)

    def pop(self):
        return self.linkedlist.pop()

    def isEmpty(self):
        return self.linkedlist.isEmpty()

    def peek(self):
        return self.linkedlist.get_value(self.linkedlist.length() - 1)

    def size(self):
        return self.linkedlist.length()


class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()
        self.current = 0;
        self.limit = 5

    def isEmpty(self):
        return self.linkedlist.isEmpty()

    def enQueue(self, input):
        if self.current == self.limit:
            return
        self.current += 1
        self.linkedlist.append(input)

    def deQueue(self):
        self.current -= 1
        self.linkedlist.poppos(0)

    def isFull(self):
        if self.current == self.limit:
            return True
        else :
            return False

    def traversal(self):
        self.linkedlist.traversal();

    def peek(self):
        return self.linkedlist.get_value(0)

    def size(self):
        return self.linkedlist.length()


queue = Queue()
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)
queue.enQueue(4)
queue.enQueue(5)
queue.enQueue(6)
queue.deQueue()
print("Peak", queue.peek())
queue.traversal()

firstNode

1. def prt(self, Node current):
        prt (current.left)
2.    print value at node

4.     ptr (current.right)

5. prt(firstNode)
