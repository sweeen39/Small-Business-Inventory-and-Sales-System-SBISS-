def find_product(products, product_id):
    for product in products:
        if product["product_id"].lower() == product_id.lower():
            return product
    return None

def add_product(products):
    """Add a new product after validating all product information."""
    print("\n--- Add New Product ---")

    while True:
        product_id = input("Enter Product ID: ").strip()
        if product_id == "":
            print("Error: Product ID cannot be empty.")
        elif find_product(products, product_id) is not None:
            print("Error: This Product ID already exists.")
        else:
            break

    name = input("Enter Product Name: ").strip()
    while name == "":
        print("Error: Product name cannot be empty.")
        name = input("Enter Product Name: ").strip()

    category = input("Enter Category: ").strip()
    while category == "":
        print("Error: Category cannot be empty.")
        category = input("Enter Category: ").strip()

    while True:
        try:
            cost_price = float(input("Enter Cost Price (RM): "))
            if cost_price <= 0:
                print("Error: Cost price must be greater than 0.")
            else:
                break
        except ValueError:
            print("Error: Please enter a valid number.")

    while True:
        try:
            selling_price = float(input("Enter Selling Price (RM): "))
            if selling_price < cost_price:
                print("Error: Selling price cannot be lower than cost price.")
            else:
                break
        except ValueError:
            print("Error: Please enter a valid number.")

    while True:
        try:
            stock = int(input("Enter Initial Stock Quantity: "))
            if stock < 0:
                print("Error: Stock cannot be negative.")
            else:
                break
        except ValueError:
            print("Error: Please enter a whole number.")

    new_product = {
        "product_id": product_id,
        "name": name,
        "category": category,
        "cost_price": round(cost_price, 2),
        "selling_price": round(selling_price, 2),
        "stock": stock,
        "units_sold": 0
    }
    products.append(new_product)
    print("Success: Product", product_id, "added.")


def display_products(products):
    """Print all products in a simple table."""
    print("\n--- Product List ---")

    if len(products) == 0:
        print("No products available.")
        return

    print(
        f"{'ID':<8}"
        f"{'Name':<20}"
        f"{'Category':<15}"
        f"{'Cost':>6}"
        f"{'Price':>11}"
        f"{'Stock':>12}"
        f"{'Sold':>8}"
    )
    print("-" * 81)

    for product in products:
        print(f"{product['product_id']:<8}"
              f"{product['name']:<20}"
              f"{product['category']:<15}"
              f"{'RM ' + format(product['cost_price'], '.2f'):>10}"
              f"{'RM ' + format(product['selling_price'], '.2f'):>10}"
              f"{product['stock']:>8}"
              f"{product['units_sold']:>8}")


def search_product(products):
    """Search products by product ID, name or category."""
    print("\n--- Search Product ---")

    if len(products) == 0:
        print("No products available.")
        return

    print("Search by:")
    print("1. Product ID")
    print("2. Product Name")
    print("3. Category")
    choice = input("Enter your choice (1-3): ").strip()
    keyword = input("Enter search keyword: ").strip().lower()

    found_products = []

    if choice == "1":
        for product in products:
            if product["product_id"].lower() == keyword:
                found_products.append(product)

    elif choice == "2":
        for product in products:
            if keyword in product["name"].lower():
                found_products.append(product)

    elif choice == "3":
        for product in products:
            if keyword in product["category"].lower():
                found_products.append(product)

    else:
        print("Error: Invalid choice.")
        return

    if len(found_products) == 0:
        print("No matching product found.")
    else:
        print(f"\n{'ID':<8}{'Name':<20}{'Category':<15}{'Cost':>8}{'Price':>8}{'Stock':>8}{'Sold':>8}")
        print("-" * 75)
        for product in found_products:
            print(f"{product['product_id']:<8}"
                  f"{product['name']:<20}"
                  f"{product['category']:<15}"
                  f"{product['cost_price']:>8.2f}"
                  f"{product['selling_price']:>8.2f}"
                  f"{product['stock']:>8}"
                  f"{product['units_sold']:>8}")


def update_product(products):
    """Update information for an existing product."""
    print("\n--- Update Product ---")

    if len(products) == 0:
        print("No products available.")
        return

    product_id = input("Enter Product ID to update: ").strip()
    product = find_product(products, product_id)

    if product is None:
        print("Error: Product not found.")
        return

    print("Leave a field blank to keep the current value.")

    new_name = input(f"New Name [{product['name']}]: ").strip()
    if new_name != "":
        product["name"] = new_name

    new_category = input(f"New Category [{product['category']}]: ").strip()
    if new_category != "":
        product["category"] = new_category

    new_cost = input(f"New Cost Price [{product['cost_price']:.2f}]: ").strip()

    new_price = input(f"New Selling Price [{product['selling_price']:.2f}]: ").strip()

    # Keep the current values first
    updated_cost = product["cost_price"]
    updated_price = product["selling_price"]

    # Check the new cost price
    if new_cost != "":
        try:
            updated_cost = float(new_cost)

            if updated_cost <= 0:
                print("Error: Cost price must be greater than 0.")
                return

            updated_cost = round(updated_cost, 2)

        except ValueError:
            print("Error: Invalid cost price.")
            return

    # Check the new selling price
    if new_price != "":
        try:
            updated_price = float(new_price)

            if updated_price <= 0:
                print("Error: Selling price must be greater than 0.")
                return

            updated_price = round(updated_price, 2)

        except ValueError:
            print("Error: Invalid selling price.")
            return

    # Compare the final cost price and selling price
    if updated_price < updated_cost:
        print("Error: Selling price cannot be lower than cost price.")
        return

    # Update only after all validation passes
    product["cost_price"] = updated_cost
    product["selling_price"] = updated_price

    new_stock = input(f"New Stock Quantity [{product['stock']}]: ").strip()
    if new_stock != "":
        try:
            new_stock = int(new_stock)
            if new_stock < 0:
                print("Error: Stock cannot be negative. Not changed.")
            else:
                product["stock"] = new_stock
        except ValueError:
            print("Error: Invalid whole number. Stock not changed.")

    print("Success: Product updated.")


def delete_product(products):
    """Delete a product, but only after the user confirms."""
    print("\n--- Delete Product ---")

    if len(products) == 0:
        print("No products available.")
        return

    product_id = input("Enter Product ID to delete: ").strip()
    product = find_product(products, product_id)

    if product is None:
        print("Error: Product not found.")
        return

    confirm = input(f"Delete '{product['name']}'? (Y/N): ").strip().lower()

    if confirm == "y":
        products.remove(product)
        print("Success: Product deleted.")
    else:
        print("Cancelled. Product was not deleted.")


def restock_product(products):
    """Add a positive quantity to an existing product's stock."""
    print("\n--- Restock Product ---")

    if len(products) == 0:
        print("No products available.")
        return

    product_id = input("Enter Product ID to restock: ").strip()
    product = find_product(products, product_id)

    if product is None:
        print("Error: Product not found.")
        return

    while True:
        try:
            qty = int(input("Enter quantity to add: "))
            if qty <= 0:
                print("Error: Quantity must be a positive number.")
            else:
                product["stock"] = product["stock"] + qty
                print("Success: New stock level is", product["stock"])
                break
        except ValueError:
            print("Error: Please enter a whole number.")

if __name__ == "__main__":
    products = []

    while True:
        print("\n=== Inventory Test Menu ===")
        print("1. Add product")
        print("2. Display products")
        print("3. Search product")
        print("4. Update product")
        print("5. Delete product")
        print("6. Restock product")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_product(products)
        elif choice == "2":
            display_products(products)
        elif choice == "3":
            search_product(products)
        elif choice == "4":
            update_product(products)
        elif choice == "5":
            delete_product(products)
        elif choice == "6":
            restock_product(products)
        elif choice == "7":
            print("Exiting.")
            break
        else:
            print("Error: Invalid option. Choose 1-7.")