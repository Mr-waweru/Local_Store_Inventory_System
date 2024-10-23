# main.py
from product_functions import *

def main_menu():
    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Low Stock Alert")
        print("6. Search Product by Name")
        print("7. Sort Products")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            add_products()
        elif choice == '2':
            view_products()
        elif choice == '3':
            update_product()
        elif choice == '4':
            delete_product()
        elif choice == '5':
            low_stock_alert()
        elif choice == '6':
            search_by_name()
        elif choice == '7':
            sort_product()
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please select again.")

if __name__ == "__main__":
    main_menu()
