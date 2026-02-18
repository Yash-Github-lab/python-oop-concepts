from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    """Abstract class for database connections"""
    
    @abstractmethod
    def connect(self):
        """Establish connection"""
        pass
    
    @abstractmethod
    def execute_query(self, query):
        """Execute a query"""
        pass
    
    @abstractmethod
    def close(self):
        """Close connection"""
        pass


class MySQLConnection(DatabaseConnection):
    """MySQL implementation"""
    
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.connected = False
    
    def connect(self):
        self.connected = True
        return f"Connected to MySQL at {self.host}"
    
    def execute_query(self, query):
        if self.connected:
            return f"MySQL executing: {query}"
        return "Not connected"
    
    def close(self):
        self.connected = False
        return "MySQL connection closed"


class PostgreSQLConnection(DatabaseConnection):
    """PostgreSQL implementation"""
    
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.connected = False
    
    def connect(self):
        self.connected = True
        return f"Connected to PostgreSQL at {self.host}"
    
    def execute_query(self, query):
        if self.connected:
            return f"PostgreSQL executing: {query}"
        return "Not connected"
    
    def close(self):
        self.connected = False
        return "PostgreSQL connection closed"


# Usage
mysql = MySQLConnection("localhost", "root", "password")
print(mysql.connect())
print(mysql.execute_query("SELECT * FROM users"))
print(mysql.close())

print()

postgres = PostgreSQLConnection("localhost", "admin", "password")
print(postgres.connect())
print(postgres.execute_query("SELECT * FROM users"))
print(postgres.close())
