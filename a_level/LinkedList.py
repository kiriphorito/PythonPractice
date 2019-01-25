class LinkedList:
    def __init__(self):
        self.first_node = None

    def add(self, value):
        '''
        if self.first_node is None:
            self.first_node = Node(value, None)
        else:
            current = self.first_node
            while current.next is not None:
                current = current.next
            current.next = Node(value, None)
            '''
        if self.first_node is None:
            self.first_node = Node(value, None)
            return
        current = self.first_node
        while current.next is not None:
            current = current.next
        current.next = Node(value, None)

    def traverse(self):
        current = self.first_node
        while (current != None):
            print(current.value)
            current = current.next
        print()

    # Deletes the first node with the value inputed
    def delete(self, value):
        current = self.first_node
        # If the first node contains the value then point the first node to the second node
        if self.first_node.value == value:
            self.first_node = self.first_node.next
            return
        # Loop until you see the value to remove in the next node or you are at the end of the list
        while True:
            # If you are at the end of the list
            if current.next is None:
                print("The number", value, "doesn't exist in the list")
                return
            # If the value of the next node is the one you are looking for
            elif current.next.value == value:
                break
            else:
                current = current.next
        # Remove the reference and the Node will be removed by the Garbage Collector
        current.next = current.next.next

    def delete_at(self, position):
        current = self.first_node
        if position == 0:
            self.first_node = current.next
            return
        for x in range (0, position - 1):
            current = current.next
        current.next = current.next.next

    def insert(self, value, position):
        current = self.first_node
        if position == 0:
            new_node = Node(value, current)
            self.first_node = new_node
            return
        for x in range (1 , position):
            current = current.next
        new_node = Node(value, current.next)
        current.next = new_node

class Node:
    def __init__(self, value, pointer):
        self.value = value
        self.next = pointer


list = LinkedList()
list.add("Sam")
list.add("Fletcher")
list.add("Gemma")

list.traverse()
list.insert("Hello",0)

list.traverse()

