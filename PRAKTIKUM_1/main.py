class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

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

    def findLMISElements(self):
        return self._findLMISElements(self.root, float('-inf'), [])

    def _findLMISElements(self, node, prev, current_sequence):
        if node is None:
            return current_sequence

        if node.key > prev:
            left_sequence = self._findLMISElements(node.left, node.key, current_sequence + [node.key])
            right_sequence = self._findLMISElements(node.right, node.key, current_sequence + [node.key])
            return left_sequence if len(left_sequence) > len(right_sequence) else right_sequence
        else:
            left_sequence = self._findLMISElements(node.left, node.key, [node.key])
            right_sequence = self._findLMISElements(node.right, node.key, [node.key])
            return left_sequence if len(left_sequence) > len(right_sequence) else right_sequence

# Usage example
bst = BinarySearchTree()
keys = [9, 1, 5, 4, 6, 3, 7, 2, 10, 8]
for key in keys:
    bst.insert(key)

print("Largest Monotonically Increasing Sequence:", bst.findLMISElements())
print("Length of LMIS:", len(bst.findLMISElements()))
