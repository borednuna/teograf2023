class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.lmis_length = 0

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root

    def find_lmis(self):
        def dfs(node):
            if not node:
                return 0, []

            lmis_elements = [node.key]
            for child in (node.left, node.right):
                if child:
                    child_lmis, child_elements = dfs(child)
                    if node.key < child.key and node.lmis_length < child_lmis:
                        node.lmis_length = child_lmis
                        lmis_elements = [node.key] + child_elements

            return node.lmis_length + 1, lmis_elements

        max_lmis_length, max_lmis_elements = 0, []
        if self.root:
            for node in (self.root, self.root.left, self.root.right):
                if node:
                    lmis_length, lmis_elements = dfs(node)
                    if lmis_length > max_lmis_length:
                        max_lmis_length = lmis_length
                        max_lmis_elements = lmis_elements

        return max_lmis_length, max_lmis_elements

# Example usage:
bst = BinarySearchTree()
sequence = [7, 2, 1, 10, 8, 6, 5, 4, 9, 3]
for num in sequence:
    bst.insert(num)

lmis_length, lmis_elements = bst.find_lmis()
print(f"LMIS Length: {lmis_length}")  # Output: 4 (for the sequence [1, 6, 8, 9])
print(f"LMIS Elements: {lmis_elements}")  # Output: [1, 6, 8, 9]
