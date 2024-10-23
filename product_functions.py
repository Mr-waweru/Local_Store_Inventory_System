from connection import connect_to_db
from product import Product


def add_products():
    db = connect_to_db()    # Connect to the db
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    stock_quantity = input("Enter stock quantity: ")
    price = float(input("Enter price: "))

    product = Product(name, category, stock_quantity, price)    # Creating a new object
    product.save_to_db(db)
    print(f"{name} Product added successfully.")
    db.close()  # Close the db connection


def view_products():
    db = connect_to_db()
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()    # Get all products

    for product in products:
        print(f"ID: {product['id']}, Name: {product['name']}, Category: {product['category']}, Stock: {product['stock_quantity']}, Price: {product['price']}")
    db.close()


def update_product():
    db = connect_to_db()
    product_id = int(input("Enter product ID to update: "))
    name = input("Enter new product name: ")
    category = input("Enter new product category: ")
    price = float(input("Enter new price: "))

    with db.cursor() as cursor:
        sql = "UPDATE products SET names=%s, category=%s, price=%s WHERE id=%s"
        cursor.execute(sql, (name, category, price, product_id))    # Update product details
    db.commit()
    price(f"Product {product_id} updated successfully.")
    db.close()


def delete_product():
    db = connect_to_db()
    product_id = int(input("Enter product ID to delete: "))

    with db.cursor() as cursor:
        cursor.execute("DELETE FROM products WHERE id=%s", (product_id))
    db.commit()
    print(f"Product {product_id} deleted successfully.")    
    db.close()


def low_stock_alert(threshold=5):
    db = connect_to_db()
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM products WHERE stock_quantity < %s", (threshold,)) #  (threshold,) single-element tuple hence , after
        low_stock_products = cursor.fetchall()     # Get products below threshold
    
    if low_stock_products:
        for product in low_stock_products:
            print(f"Low stock alert for {product['name']}. Only {product['stock_quantity']} left.")
    else:
        print("All products are well-stocked.")
    db.close()


def search_by_name():
    db = connect_to_db()
    search_name = input("Enter product to search: ")
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM products WHERE name LIKE %s", ('%' + search_name + '%',))
        products = cursor.fetchall()

    for product in products:
        print(f"ID: {product['id']}, Name: {product['name']}, Category: {product['category']}, Stock: {product['stock_quantity']}, Price: {product['price']}")
    db.close()


def sort_product():
    db = connect_to_db()
    sort_by = input("Sort by (stock_quantity/price: )")

    sql = f"SELECT * FROM products ORDER BY {sort_by}"
    with db.cursor() as cursor:
        cursor.execute(sql)
        sorted_products = cursor.fetchall()

    for product in sorted_products:
        print(f"ID: {product['id']}, Name: {product['name']}, Category: {product['category']}, Stock: {product['stock_quantity']}, Price: {product['price']}")
    db.close()
