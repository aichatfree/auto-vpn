from peewee import (
    SqliteDatabase,
    PostgresqlDatabase,
    Proxy,
)
from urllib.parse import urlparse
from contextlib import contextmanager

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.initialized = False
            cls._instance.proxy = Proxy() 
        return cls._instance

    def init_db(self, db_url: str = 'sqlite:///data_layer.db'):
        print(f"Initializing database with URL: {db_url}")
        parsed_url = urlparse(db_url)
        
        if parsed_url.scheme == 'sqlite':
            pragmas = {
                'foreign_keys': 1,
                'journal_mode': 'wal',
                'cache_size': -1024 * 64,
            }
            path = parsed_url.path[1:] if parsed_url.path.startswith('/') else parsed_url.path
            database = SqliteDatabase(path, pragmas=pragmas)
        
        elif parsed_url.scheme == 'postgresql':
            database = PostgresqlDatabase(
                database=parsed_url.path.lstrip('/'),
                user=parsed_url.username,
                password=parsed_url.password,
                host=parsed_url.hostname,
                port=parsed_url.port or 5432,
            )
        else:
            raise ValueError("Unsupported database scheme. Use 'sqlite' or 'postgresql'.")

        self.proxy.initialize(database)
        self.db = database
        self.initialized = True
        
        from auto_vpn.db.models import BaseModel, Server, VPNPeer, Setting
        self.db.create_tables([Server, VPNPeer, Setting])

    @contextmanager
    def connection(self):
        if not self.initialized:
            raise RuntimeError("Database not initialized. Call init_db first.")
        
        # Check if connection is already open
        if not self.db.is_closed():
            # Use existing connection
            yield
        else:
            # Open new connection
            try:
                self.db.connect()
                yield
            finally:
                if not self.db.is_closed():
                    self.db.close()

db_instance = Database()

