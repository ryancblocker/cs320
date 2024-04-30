
class Node:
    def __init__(self, keys=None, children=None, parent=None):
        self.keys = keys if keys is not None else []
        self.children = children if children is not None else []
        self.parent = parent

    def __repr__(self):
        return f"Node(keys={self.keys})"

class BTree:
    def __init__(self, max_size=4):
        self.root = Node()
        self.max_size = max_size

    def insert(self, value):
        if not self.root.keys:
            self.root.keys.append(value)
        else:
            self._insert(value, self.root)

    
    def _insert(self, value, node):
        i = 0
        while i < len(node._keys) and node._keys[i] < value:
            i += 1
        if not node._children:
            node._keys.insert(i, value)
            if len(node._keys) > self.max_size:
                self._split(node)
        else:
            self._insert(value, node._children[i])

def __str__(self):
    return self._print_tree(self.root)

def _print_tree(self, node, level=0):
    ret = "\t" * level + repr(node.keys) + "\n"
    for child in node.children:
        ret += self._print_tree(child, level + 1)
    return ret

class Utility:
    @staticmethod
    def search(tree, value):
        # Search logic (simplified for brevity)
        return False

    @staticmethod
    def traverse(tree):
        # Traverse logic (simplified for brevity)
        pass

# Example usage
btree = BTree()
btree.insert(10)
btree.insert(20)
btree.insert(5)
print(btree)
