CREATE DATABASE inventory_db;

USE inventory_db;


CREATE TABLE IF NOT EXISTS products(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(100),
    stock_quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);


INSERT INTO products (name, category, stock_quantity, price)
VALUES
('Milk', 'Groceries', 100, 50.00),
('Bread', 'Groceries', 50, 30.00),
('TV', 'Electronics', 10, 500.00),
('Laptop', 'Electronics', 5, 1000.00);

SELECT * FROM products: