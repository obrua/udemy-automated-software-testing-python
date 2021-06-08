from typing import Any, Iterable

class Cursor:
    arraysize: int
    binary_types: Any = ...
    closed: Any = ...
    connection: Any = ...
    description: Any = ...
    itersize: int
    lastrowid: int
    name: Any = ...
    query: str
    row_factory: Any = ...
    rowcount: int
    rownumber: int
    scrollable: Any = ...
    statusmessage: str
    string_types: Any = ...
    typecaster: Any = ...
    tzinfo_factory: Any = ...
    withhold: Any = ...
    def __init__(self, *args: Any, **kwargs: Any): ...
    def callproc(self, procname: Any, parameters: Any=None): ...
    def cast(self, oid: Any, s: Any): ...
    def close(self): ...
    def copy_expert(self, sql: Any, file: Any, size: Any=8192): ...
    def copy_from(self, *args: Any, **kwargs: Any): ...
    def copy_to(self, *args: Any, **kwargs: Any): ...
    def execute(self, query: str, vars: Any=None): ...
    def executemany(self, query: str, vars_list: Any): ...
    def fetchall(self) -> Iterable[Any]: ...
    def fetchmany(self, *args: Any, **kwargs: Any) -> Iterable[Any]: ...
    def fetchone(self) -> list[Any]: ...
    def mogrify(self, query:str, vars: Any=None): ...
    def nextset(self): ...
    def scroll(self, *args: Any, **kwargs: Any): ...
    def setinputsizes(self, sizes: Any): ...
    def setoutputsize(self, size: Any, column: Any=None): ...
    def __enter__(self, *args: Any, **kwargs: Any) -> "Cursor": ...
    def __exit__(self, *args: Any, **kwargs: Any): ...
    def __iter__(self): ...
    def __next__(self): ...

class Connection:
    DataError: Any = ...
    DatabaseError: Any = ...
    Error: Any = ...
    IntegrityError: Any = ...
    InterfaceError: Any = ...
    InternalError: Any = ...
    NotSupportedError: Any = ...
    OperationalError: Any = ...
    ProgrammingError: Any = ...
    Warning: Any = ...
    # async: Any = ...
    async_: Any = ...
    autocommit: Any = ...
    binary_types: Any = ...
    closed: Any = ...
    cursor_factory: Any = ...
    deferrable: Any = ...
    dsn: Any = ...
    encoding: Any = ...
    isolation_level: Any = ...
    notices: Any = ...
    notifies: Any = ...
    protocol_version: Any = ...
    readonly: Any = ...
    server_version: Any = ...
    status: Any = ...
    string_types: Any = ...
    def __init__(self, *args: Any, **kwargs: Any): ...
    def cancel(self): ...
    def close(self): ...
    def commit(self): ...
    def cursor(self, *args: Any, **kwargs: Any) -> "Cursor": ...
    def fileno(self): ...
    def get_backend_pid(self): ...
    def get_dsn_parameters(self): ...
    def get_parameter_status(self, parameter: Any): ...
    def get_transaction_status(self): ...
    def isexecuting(self): ...
    def lobject(self, *args: Any, **kwargs: Any): ...
    def poll(self): ...
    def reset(self): ...
    def rollback(self): ...
    def set_client_encoding(self, encoding: Any): ...
    def set_isolation_level(self, level: Any): ...
    def set_session(self, *args: Any, **kwargs: Any): ...
    def tpc_begin(self, xid: Any): ...
    def tpc_commit(self, *args: Any, **kwargs: Any): ...
    def tpc_prepare(self): ...
    def tpc_recover(self): ...
    def tpc_rollback(self, *args: Any, **kwargs: Any): ...
    def xid(self, format_id: Any, gtrid: Any, bqual: Any): ...
    def __enter__(self, *args: Any, **kwargs: Any): ...
    def __exit__(self, *args: Any, **kwargs: Any): ...


class SimpleConnectionPool:
    def getconn(self) -> Connection: ...
    def putconn(self, connection: Connection): ...