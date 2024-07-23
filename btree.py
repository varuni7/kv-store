from typing import List, Optional, Tuple
import threading

class Node:
    def __init__(self, is_leaf: bool = True):
        self.keys: List[str] = []
        self.values: List[str] = []
        self.children: List['Node'] = []
        self.is_leaf = is_leaf

class BTree:
    def __init__(self):
        self.root = Node()
        self.lock = threading.RLock()

    def insert(self, key: str, value: str):
        with self.lock:
            if not self.root.keys:
                self.root.keys.append(key)
                self.root.values.append(value)
                return

            self._insert(self.root, key, value)

    def _insert(self, node: Node, key: str, value: str):
        if node.is_leaf:
            node.keys.append(key)
            node.values.append(value)
            node.keys, node.values = zip(*sorted(zip(node.keys, node.values)))
            node.keys = list(node.keys)
            node.values = list(node.values)
            return

        # Simplified: Always insert into the first child
        self._insert(node.children[0], key, value)

    def get(self, key: str) -> Tuple[Optional[str], bool]:
        with self.lock:
            return self._get(self.root, key)

    def _get(self, node: Node, key: str) -> Tuple[Optional[str], bool]:
        for i, k in enumerate(node.keys):
            if k == key:
                return node.values[i], True

        if node.is_leaf:
            return None, False

        # Simplified: Always search in the first child
        return self._get(node.children[0], key)

    def __str__(self):
        with self.lock:
            return str(self.root)