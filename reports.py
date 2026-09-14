def generate_reports(products, sales):
    """Display all business reports."""

    print("\n========== BUSINESS REPORT ==========")

    inventory_summary(products)
    low_stock_report(products)
    out_of_stock_report(products)
    sales_summary(sales)
    gross_profit_summary(sales)
    best_selling_product(products)
    highest_value_transaction(sales)
    category_summary(products)

    print("\n=====================================")


def inventory_summary(products):
    """
    Display total products, total stock units
    and total inventory cost value.
    """

    print("\n--- Inventory Summary ---")

    if not products:
        print("No product records found.")
        return

    total_products = len(products)
    total_stock = sum(product["stock"] for product in products)
    inventory_cost = sum(product["stock"] * product["cost_price"] for product in products)

    print(f"Total Products      : {total_products}")
    print(f"Total Stock Units   : {total_stock}")
    print(f"Inventory Cost Value: RM {inventory_cost:.2f}")


def low_stock_report(products):
    """
    Display products with stock levels
    below the selected threshold.
    """

    print("\n--- Low Stock Report ---")

    if not products:
        print("No product records found.")
        return

    try:
        threshold = int(input("Enter stock threshold: "))

        if threshold < 0:
            print("Threshold cannot be negative.")
            return

    except ValueError:
        print("Invalid threshold.")
        return

    found = False

    for product in products:
        if product["stock"] < threshold:
            found = True
            print(
                f'{product["product_id"]} | '
                f'{product["name"]} | '
                f'Stock: {product["stock"]}'
            )

    if not found:
        print("No low stock products.")


def out_of_stock_report(products):
    """
    Display products that have zero
    stock quantity.
    """

    print("\n--- Out of Stock Report ---")

    if not products:
        print("No product records found.")
        return

    found = False

    for product in products:
        if product["stock"] == 0:
            found = True
            print(
                f'{product["product_id"]} | '
                f'{product["name"]}'
            )

    if not found:
        print("No out-of-stock products.")


def sales_summary(sales):
    """
    Display completed sales transactions
    and calculate total revenue.
    """

    print("\n--- Sales Summary ---")

    if not sales:
        print("No sales records found.")
        return

    transactions = len(sales)
    revenue = sum(
        sale["subtotal"] - sale["discount_amount"]  #This function calculates the number of 
        for sale in sales                         #completed transactions and total sales revenue.
    )

    print(f"Completed Transactions : {transactions}")
    print(f"Sales Revenue          : RM {revenue:.2f}")


def gross_profit_summary(sales):
    """
    Calculate and display the total gross
    profit from completed sales.
    """

    print("\n--- Gross Profit Summary ---")

    if not sales:
        print("No sales records found.")
        return

    total_profit = sum(sale["gross_profit"] for sale in sales)

    print(f"Gross Profit : RM {total_profit:.2f}")


def best_selling_product(products):
    """
    Identify and display the product
    with the highest units sold.
    """

    print("\n--- Best Selling Product ---")

    if not products:
        print("No product records found.")
        return

    if all(product["units_sold"] == 0 for product in products):
        print("No products have been sold yet.")
        return

    best = max(products, key=lambda product: product["units_sold"])

    print(f"Product Name : {best['name']}")
    print(f"Product ID   : {best['product_id']}")
    print(f"Units Sold   : {best['units_sold']}")


def highest_value_transaction(sales):
    """
    Identify and display the transaction
    with the highest total value.
    """

    print("\n--- Highest Value Transaction ---")

    if not sales:
        print("No sales records found.")
        return

    highest = max(sales, key=lambda sale: sale["total"]) #max() finds the product with the highest units_sold.
                #lambda tells max() to compare the products based on their units_sold value.
    print(f"Sale ID : {highest['sale_id']}")    
    print(f"Total   : RM {highest['total']:.2f}")


def category_summary(products):
    """
    Generate a summary of products
    grouped by category.
    """

    print("\n--- Category Summary ---")

    if not products:
        print("No product records found.")
        return

    unique_categories = set()

    for product in products:
        unique_categories.add(product["category"])

    for category in sorted(unique_categories):
        count = 0

        for product in products:
            if product["category"] == category:
                count += 1

        print(f"{category}: {count} product(s)")

if __name__ == "__main__":

    test_products = [
        {
            "product_id": "P001",
            "name": "Wireless Mouse",
            "category": "Accessories",
            "cost_price": 25.00,
            "selling_price": 39.90,
            "stock": 3,
            "units_sold": 20
        },

        {
            "product_id": "P002",
            "name": "Keyboard",
            "category": "Accessories",
            "cost_price": 50.00,
            "selling_price": 80.00,
            "stock": 0,
            "units_sold": 10
        },

        {
            "product_id": "P003",
            "name": "Laptop",
            "category": "Electronics",
            "cost_price": 1000.00,
            "selling_price": 1500.00,
            "stock": 10,
            "units_sold": 5
        }
    ]

    test_sales = [
        {
            "sale_id": "S001",
            "subtotal": 200.00,
            "discount_amount": 20.00,
            "total": 190.80,
            "gross_profit": 50.00
        },

        {
            "sale_id": "S002",
            "subtotal": 500.00,
            "discount_amount": 75.00,
            "total": 450.50,
            "gross_profit": 150.00
        }
    ]

    generate_reports(test_products, test_sales)
