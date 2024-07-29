from enum import Enum, auto
from typing import Dict

class QueryType(Enum):
    INSERT = auto()
    SELECT = auto()

class Query:
    def __init__(self, query_type: QueryType, table: str, values: Dict[str, str] = None, where: Dict[str, str] = None):
        self.type = query_type
        self.table = table
        self.values = values or {}
        self.where = where or {}

def parse(query_str: str) -> Query:
    parts = query_str.split()
    if len(parts) < 4:
        raise ValueError("Invalid query")

    query_type = parts[0].upper()
    table = parts[2]

    if query_type == "INSERT":
        if len(parts) < 6 or parts[3].upper() != "VALUES":
            raise ValueError("Invalid INSERT query")
        values = {
            "id": parts[4].strip("(,)"),
            "name": parts[5].strip("(,)")
        }
        return Query(QueryType.INSERT, table, values=values)

    elif query_type == "SELECT":
        where = {}
        if len(parts) > 4 and parts[4].upper() == "WHERE":
            where["id"] = parts[6]
        return Query(QueryType.SELECT, table, where=where)

    else:
        raise ValueError("Unsupported query type")