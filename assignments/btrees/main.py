class BTree:
    def __init__(self, keys=None, children=None, max_size=4, parent=None):
        self._keys = keys if keys is not None else []
        self._children = children if children is not None else []
        self.max_size = max_size
        self.parent = parent

    def __repr__(self):
        return self.__str__()

    def string(self, level=0):
        ret = "\t" * level + repr(self._keys) + ", level: " + str(level) + "\n"
        for child in self._children:
            ret += child.string(level + 1)
        return ret

    def __str__(self):
        if not self._keys and not self._children:
            return "Empty BTree"
        return self.string()

    def keys(self):
        return self._keys

    def children(self):
        return self._children
    
    #start here

    def insert(self, value):
        if value is None or self.contains(value):
            return
        if not self._keys:
            self._keys.append(value)
        else:
            self._insert(value, self)

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

    def _split(self, node):
        mid_index = len(node._keys) // 2
        left_keys = node._keys[:mid_index]
        right_keys = node._keys[mid_index + 1:]
        mid_value = node._keys[mid_index]
        left = BTree(left_keys, [], self.max_size, node.parent)
        right = BTree(right_keys, [], self.max_size, node.parent)

        if node._children:
            left._children = node._children[:mid_index + 1]
            right._children = node._children[mid_index + 1:]
            for child in left._children:
                child.parent = left
            for child in right._children:
                child.parent = right

        if node.parent:
            index = node.parent._children.index(node)
            node.parent._children[index:index+1] = [left, right]
            node.parent._keys.insert(index, mid_value)
            if len(node.parent._keys) > self.max_size:
                self._split(node.parent)
        else:
            self._keys = [mid_value]
            self._children = [left, right]
            left.parent = right.parent = self
        node.parent = None

    def contains(self, target_value):
        def search(node):
            i = 0
            while i < len(node._keys) and target_value > node._keys[i]:
                i += 1
            if i < len(node._keys) and node._keys[i] == target_value:
                return True
            if node._children:
                return search(node._children[i])
            return False
        return search(self)
    
    def traverse(self):
        def _in_order_traversal(node):
            if node is None:
                return []
            result = []
            if node._children:
                for i in range(len(node._keys)):
                    result.extend(_in_order_traversal(node._children[i]))
                    result.append(node._keys[i])
                result.extend(_in_order_traversal(node._children[-1]))
            else:
                result.extend(node._keys)
            return result

        result = _in_order_traversal(self)
        return tuple(result) if result else None
    
    def delete(self, value):
        if value is None:
            return False
        return self._delete(value, self)

    def _delete(self, value, node):
        i = 0
        while i < len(node._keys) and node._keys[i] < value:
            i += 1
        if i < len(node._keys) and node._keys[i] == value:
            if not node._children:
                node._keys.pop(i)
                if len(node._keys) < 1 and node != self:
                    self._handle_underflow(node)
            else:
                if len(node._children[i + 1]._keys) == 0:
                    self._handle_underflow(node._children[i + 1])
                successor = self._get_successor(node._children[i + 1])
                node._keys[i] = successor
                self._delete(successor, node._children[i + 1])
        elif node._children:
            self._delete(value, node._children[i])
            if len(node._children[i]._keys) < 1 and node._children[i] != self:
                self._handle_underflow(node._children[i])
        else:
            return False
        return True

    def _get_successor(self, node):
        current = node
        while current._children:
            current = current._children[0]
        if current._keys:
            return current._keys[0]
        raise Exception("No successor found, likely due to an empty node being accessed")

    def _handle_underflow(self, node):
        parent = node.parent
        if not parent:
            if len(node._keys) == 0 and len(node._children) == 1:
                new_root = node._children[0]
                self._keys, self._children = new_root._keys, new_root._children
                self.parent = None
                for child in self._children:
                    child.parent = self
            return

        index = parent._children.index(node)
        left_sibling = parent._children[index - 1] if index > 0 else None
        right_sibling = parent._children[index + 1] if index < len(parent._children) - 1 else None

        if left_sibling and len(left_sibling._keys) > (self.max_size // 2):
            node._keys.insert(0, parent._keys[index - 1])
            parent._keys[index - 1] = left_sibling._keys.pop()
            if left_sibling._children:
                node._children.insert(0, left_sibling._children.pop())
                node._children[0].parent = node
        elif right_sibling and len(right_sibling._keys) > (self.max_size // 2):
            node._keys.append(parent._keys[index])
            parent._keys[index] = right_sibling._keys.pop(0)
            if right_sibling._children:
                node._children.append(right_sibling._children.pop(0))
                node._children[-1].parent = node
        else:
            merge_with = left_sibling if left_sibling else right_sibling
            merge_index = index - 1 if left_sibling else index

            if left_sibling:
                merge_with._keys.extend([parent._keys[merge_index]] + node._keys)
                merge_with._children.extend(node._children)
            else:
                merge_with._keys[0:0] = [parent._keys[merge_index]] + node._keys
                merge_with._children[0:0] = node._children

            for child in node._children:
                child.parent = merge_with

            parent._keys.pop(merge_index)
            parent._children.pop(index)

            if len(parent._keys) < (self.max_size // 2) and parent != self:
                self._handle_underflow(parent)
