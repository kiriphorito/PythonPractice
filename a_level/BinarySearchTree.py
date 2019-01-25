class BinarySearchTree:
    def __init__(self):
        self.root_node = None

    def add(self, value):
        if self.root_node is None:
            self.root_node = Node(value)
        else:
            current = self.root_node
            while True:
                if current.value > value:
                    if current.left is None:
                        current.left = Node(value)
                        return
                    else:
                        current = current.left
                elif current.value < value:
                    if current.right is None:
                        current.right = Node(value)
                        return
                    else:
                        current = current.right
                else:
                    print("The number", value, "already exists in the tree!")
                    return

    def dfs_pre(self, node):
        print(node.value)
        if node.left is not None:
            self.dfs_pre(node.left)
        if node.right is not None:
            self.dfs_pre(node.right)

    def dfs_in(self, node):
        if node.left is not None:
            self.dfs_pre(node.left)
        print(node.value)
        if node.right is not None:
            self.dfs_pre(node.right)

    def dfs_post(self, node):
        if node.left is not None:
            self.dfs_pre(node.left)
        if node.right is not None:
            self.dfs_pre(node.right)
        print(node.value)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


tree = BinarySearchTree()
tree.add(6)
tree.add(5)
tree.add(8)
tree.add(10)
print("Pre-path")
tree.dfs_pre(tree.root_node)
print("In-path")
tree.dfs_in(tree.root_node)
print("Post-path")
tree.dfs_post(tree.root_node)
