from kvstore import KVStore
import threading

class Transaction:
    def __init__(self, store: KVStore):
        self.store = store
        self.changes = {}
        self.lock = threading.Lock()
        self.committed = False
        self.completed = threading.Event()

    def set(self, key: str, value: str):
        with self.lock:
            self.changes[key] = value

    def commit(self):
        with self.lock:
            for k, v in self.changes.items():
                self.store.set(k, v)
            self.committed = True
        self.completed.set()

    def wait(self):
        self.completed.wait()