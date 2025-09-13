import sqlite3
import time

 # part2 create a singleton pattern
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.conn = sqlite3.connect('app.db')
        return cls._instance

    def get_connection(self):
        return self.conn

def init_database():
    db_instance = DatabaseConnection()
    conn = db_instance.get_connection() # part2 Use singleton to get connection
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            product TEXT,
            amount REAL
        );
    ''')

    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Alice', 'alice@example.com'))
    cursor.execute("INSERT INTO orders (user_id, product, amount) VALUES (?, ?, ?)", (1, 'Book', 19.99))
    cursor.execute("INSERT INTO orders (user_id, product, amount) VALUES (?, ?, ?)", (1, 'Pen', 1.50))

    conn.commit()
    print("Database initialized.")


class UserService:
    def get_user(self, user_id):
        start_time = time.time()
        db_instance = DatabaseConnection()
        conn = db_instance.get_connection() # part2 Use singleton to get connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()

        end_time = time.time()
        print(f"get_user use: {end_time - start_time:.6f} second")
        return result
    
class OrderService:
    def get_orders(self, user_id):
        start_time = time.time()
        db_instance = DatabaseConnection()
        conn = db_instance.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        result = cursor.fetchall()

        end_time = time.time()
        print(f"get_orders use: {end_time - start_time:.6f} second")
        return result
    
if __name__ == "__main__":
    init_database()
    user_service = UserService()
    order_service = OrderService()
    
    user_id = 1
    user = user_service.get_user(user_id)
    print("User:", user)

    order = order_service.get_orders(user_id)
    print("Order:", order)

    DatabaseConnection().get_connection().close()
    print("Database connection closed.")