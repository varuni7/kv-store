from btree import BTree
import threading

class KVStore:
    def __init__(self):
        self.tree = BTree()
        self.lock = threading.RLock()

    def set(self, key: str, value: str):
        with self.lock:
            self.tree.insert(key, value)

    def get(self, key: str) -> str:
        with self.lock:
            value, found = self.tree.get(key)
            if found:
                return value
            raise KeyError(f"Key not found: {key}")