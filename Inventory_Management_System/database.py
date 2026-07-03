import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "Inventory_Management_System"
}

class Database:
    def __init__(self, config=None):
        self.config = config or DB_CONFIG.copy()
        self.connection = None
        self.cursor = None
        self.connected = False
        self.connect()
        if self.connected:
            self.setup_schema()

    def connect(self):
        try:
            config = self.config.copy()
            database = config.pop("database", None)
            self.connection = mysql.connector.connect(**config)
            self.cursor = self.connection.cursor(buffered=True)

            if database:
                self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{database}` DEFAULT CHARACTER SET utf8mb4")
                self.connection.database = database
                self.cursor.close()
                self.cursor = self.connection.cursor(buffered=True)

            self.connected = True
        except Error as err:
            print("Database connection error:", err)
            self.connected = False

    def setup_schema(self):
        if not self.connected:
            return

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS admins (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(100) UNIQUE NOT NULL,
                password VARCHAR(100) NOT NULL
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                category VARCHAR(255) DEFAULT '',
                quantity INT NOT NULL DEFAULT 0,
                price DECIMAL(10,2) NOT NULL DEFAULT 0.00,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        self.connection.commit()
        self.ensure_products_schema()

        self.cursor.execute("SELECT id FROM admins WHERE username=%s", ("admin",))
        if not self.cursor.fetchone():
            self.cursor.execute(
                "INSERT INTO admins (username, password) VALUES (%s, %s)",
                ("admin", "admin123")
            )
            self.connection.commit()

    def check_login(self, username, password):
        if not self.connected:
            return False

        query = "SELECT id FROM admins WHERE username=%s AND password=%s"
        self.cursor.execute(query, (username, password))
        return bool(self.cursor.fetchone())

    def add_product(self, name, category, quantity, price):
        if not self.connected:
            return False

        query = "INSERT INTO products (name, category, quantity, price) VALUES (%s, %s, %s, %s)"
        try:
            self.cursor.execute(query, (name, category, quantity, price))
            self.connection.commit()
            return True
        except Error as err:
            print("Add product error:", err)
            return False

    def get_products(self):
        if not self.connected:
            return []

        self.cursor.execute("SELECT id, name, category, quantity, price, created_at FROM products ORDER BY id DESC")
        return self.cursor.fetchall()

    def get_product_by_id(self, product_id):
        if not self.connected:
            return None

        self.cursor.execute("SELECT id, name, category, quantity, price FROM products WHERE id=%s", (product_id,))
        return self.cursor.fetchone()

    def update_product(self, product_id, name, category, quantity, price):
        if not self.connected:
            return False

        query = "UPDATE products SET name=%s, category=%s, quantity=%s, price=%s WHERE id=%s"
        self.cursor.execute(query, (name, category, quantity, price, product_id))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def delete_product(self, product_id):
        if not self.connected:
            return False

        self.cursor.execute("DELETE FROM products WHERE id=%s", (product_id,))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def search_products(self, term):
        if not self.connected:
            return []

        pattern = f"%{term}%"
        self.cursor.execute(
            "SELECT id, name, category, quantity, price, created_at FROM products "
            "WHERE name LIKE %s OR category LIKE %s ORDER BY id DESC",
            (pattern, pattern)
        )
        return self.cursor.fetchall()

    def ensure_products_schema(self):
        """Repair the products table if it has an old or invalid schema."""
        if not self.connected:
            return

        try:
            self.cursor.execute("DESCRIBE products")
            columns = {row[0] for row in self.cursor.fetchall()}
        except Error as err:
            print("Could not describe products table:", err)
            return

        expected = {'id', 'name', 'category', 'quantity', 'price', 'created_at'}
        if expected.issubset(columns):
            return

        try:
            self.cursor.execute("DROP TABLE IF EXISTS products_backup")
            self.cursor.execute("RENAME TABLE products TO products_backup")
        except Error:
            pass

        self.cursor.execute(
            """
            CREATE TABLE products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                category VARCHAR(255) DEFAULT '',
                quantity INT NOT NULL DEFAULT 0,
                price DECIMAL(10,2) NOT NULL DEFAULT 0.00,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        self.connection.commit()

        try:
            self.cursor.execute(
                "INSERT INTO products (name, category, quantity, price, created_at) "
                "SELECT name, category, quantity, price, created_at FROM products_backup "
                "WHERE name IS NOT NULL"
            )
            self.cursor.execute("DROP TABLE IF EXISTS products_backup")
            self.connection.commit()
        except Error:
            # If the old table schema does not match, leave the backup table for manual review.
            pass

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()
