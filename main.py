from inventory import (
    add_product,
    display_products,
    search_product,
    update_product,
    delete_product,
    restock_product
)

from sales import record_sale, display_sales_history
from reports import generate_reports
from utils import load_data, save_data

def display_menu():
    """Display the main menu."""

    print("\n" + "=" * 50)
    print(" SMALL BUSINESS INVENTORY AND SALES SYSTEM")
    print("=" * 50)
    print("1. Add a new product")
    print("2. Display all products")
    print("3. Search for a product")
    print("4. Update product information")
    print("5. Delete a product")
    print("6. Restock a product")
    print("7. Record a sale")
    print("8. Display sales history")
    print("9. Generate reports")
    print("10. Save data")
    print("11. Exit")
    print("=" * 50)


def main():
    """Load data, display the menu and control the program."""

    # Load existing products and sales records
    products, sales = load_data()

    while True:
        display_menu()
        choice = input("Enter your choice (1-11): ").strip()

        if choice == "1":
            add_product(products)
            save_data(products, sales)

        elif choice == "2":
            display_products(products)

        elif choice == "3":
            search_product(products)

        elif choice == "4":
            update_product(products)
            save_data(products, sales)

        elif choice == "5":
            delete_product(products)
            save_data(products, sales)

        elif choice == "6":
            restock_product(products)
            save_data(products, sales)

        elif choice == "7":
            sale = record_sale(products, sales)

            if sale is not None:
                save_data(products, sales)

        elif choice == "8":
            display_sales_history(sales)

        elif choice == "9":
            generate_reports(products, sales)

        elif choice == "10":
            save_data(products, sales)
            print("Data saved successfully.")

        elif choice == "11":
            save_data(products, sales)
            print("Data saved successfully.")
            print("Thank you for using SBISS. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 11.")


if __name__ == "__main__":
    main()