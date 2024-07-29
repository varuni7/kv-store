from kv_store import KVStore
from sql_parser import parse, QueryType

class SQLExecutor:
    def __init__(self, store: KVStore):
        self.store = store

    def execute(self, query_str: str):
        query = parse(query_str)

        if query.type == QueryType.INSERT:
            return self._execute_insert(query)
        elif query.type == QueryType.SELECT:
            return self._execute_select(query)
        else:
            raise ValueError("Unsupported query type")

    def _execute_insert(self, query):
        key = f"{query.table}:{query.values['id']}"
        self.store.set(key, query.values['name'])
        return None

    def _execute_select(self, query):
        if query.where:
            key = f"{query.table}:{query.where['id']}"
            try:
                value = self.store.get(key)
                return [{"id": query.where['id'], "name": value}]
            except KeyError:
                return []

        # Simplified: return all values (not efficient for large datasets)
        results = []
        i = 1
        while True:
            key = f"{query.table}:{i}"
            try:
                value = self.store.get(key)
                results.append({"id": str(i), "name": value})
                i += 1
            except KeyError:
                break
        return results