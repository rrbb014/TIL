""" 
Tree traversal approaches
- preorder
- inorder
- postorder
ref: https://www.tutorialspoint.com/python/python_tree_traversal_algorithms.htm
"""
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def add(self, value):
        # Add node
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.add(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.add(value)
        else:
            self.value = value
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value),
        if self.right:
            self.right.print_tree()
    
    def inorder_traversal(self, root):
        # L - root - R
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.value)
            res = res + self.inorder_traversal(root.right)
        return res
    
    def preorder_traversal(self, root):
        # root - L - R
        res = []
        if root:
            res.append(root.value)
            res = res + self.preorder_traversal(root.left)
            res = res + self.preorder_traversal(root.right)
        return res

    def postorder_traversal(self, root):
        # L - R - root
        res = []
        if root:
            res += self.postorder_traversal(root.left)
            res += self.postorder_traversal(root.right)
            res.append(root.value)
        return res


if __name__ == "__main__":
    root = Node(27)
    root.add(14)
    root.add(10)
    root.add(19)
    root.add(35)
    root.add(31)
    root.add(42)
    print(root.inorder_traversal(root))
    print(root.preorder_traversal(root))
    print(root.postorder_traversal(root))
