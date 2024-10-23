class Product:
    def __init__(self, name, category, stock_quantity, price):
        self.name = name
        self.category = category
        self.stock_quantity = stock_quantity
        self.price = price

    def save_to_db(self, db):  
        # A cursor is like a control structure that interacts with the database for query execution. 
        with db.cursor() as cursor: # db.cursor():Creates a cursor object, which execute SQL queries and fetch results from the database.
            sql = "INSERT INTO products (name, category, stock_quantity, price) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (self.name, self.category, self.stock_quantity, self.price))
        db.commit() # Saves changes to the database, ensuring product is permanently added to the products table.