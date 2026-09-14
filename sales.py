"""
sales.py
Member 3 — Sales transactions and calculations.

Expected data shapes (shared with other team members' modules):

    products : list[dict]
        Each product dict looks like:
        {
            "product_id": "P001",          # unique product id (string or int)
            "name": "Notebook",
            "selling_price": 12.50,        # selling price per unit
            "cost_price": 8.00,    # cost per unit (used for gross profit)
            "stock": 50,           # units currently in stock
            "units_sold": 0        # running total of units sold
        }

    sales : list[dict]
        Each completed transaction is appended here by record_sale().
        See generate_receipt()/record_sale() for the exact structure.
"""

import uuid
from datetime import datetime


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def _find_product(products, product_id):
    """Return the product dict matching product_id, or None if not found."""
    for product in products:
        if str(product.get("product_id", "")).lower() == str(product_id).lower():
            return product
    return None

# How to prevent duplicate sale IDs
def _generate_sale_id(sales):
    """Generate a unique sale ID."""

    while True:
        sale_id = "SALE-" + uuid.uuid4().hex[:6].upper()

        duplicate = False

        for sale in sales:
            if sale["sale_id"] == sale_id:
                duplicate = True
                break

        if not duplicate:
            return sale_id


# --------------------------------------------------------------------------
# Core calculation functions
# --------------------------------------------------------------------------

def calculate_discount(subtotal):
    """
    Calculate discount based on order subtotal.

    Discount Rules:
        Below RM100         0%
        RM100 - RM199.99    5%
        RM200 - RM499.99   10%
        RM500 and above    15%

    Returns:
        (discount_rate, discount_amount) as a tuple of floats.
    """
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")

    if subtotal >= 500:
        rate = 0.15
    elif subtotal >= 200:
        rate = 0.10
    elif subtotal >= 100:
        rate = 0.05
    else:
        rate = 0.0

    discount_amount = round(subtotal * rate, 2)
    return rate, discount_amount


def calculate_tax(amount):
    """
    Calculate the 6% simulated sales tax on the given amount
    (this should be applied AFTER discount, i.e. amount = subtotal - discount).

    Returns:
        tax_amount (float)
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
    return round(amount * 0.06, 2)


# --------------------------------------------------------------------------
# Sale recording
# --------------------------------------------------------------------------

def record_sale(products, sales):
    """
    Record a new sale transaction. Supports one or more products in a
    single transaction. Prompts the user for input, validates everything,
    updates stock/units_sold, calculates totals, generates a receipt,
    and stores the completed sale in `sales`.

    Returns:
        The completed sale dict, or None if the sale was cancelled
        (e.g. no valid items were added).
    """
    print("\n--- New Sale ---")
    print("Enter product ID and quantity for each item.")
    print("Type 'done' as the Product ID when you are finished.\n")

    items = []          # list of line-item dicts for this sale
    subtotal = 0.0
    total_cost = 0.0     # for gross profit calculation

    while True:
        product_id = input("Product ID (or 'done' to finish): ").strip()

        if product_id.lower() == "done":
            break

        # Check whether the product ID exists
        product = _find_product(products, product_id)
        if product is None:
            print(f"  ✗ No product found with ID '{product_id}'. Try again.\n")
            continue

        # Validate the sale quantity
        qty_input = input(f"  Quantity for '{product['name']}': ").strip()
        try:
            quantity = int(qty_input)
        except ValueError:
            print("  ✗ Quantity must be a whole number. Try again.\n")
            continue

        if quantity <= 0:
            print("  ✗ Quantity must be greater than zero. Try again.\n")
            continue

        # Prevent selling more than available stock
        # Check quantity already added to this sale
        reserved_qty = sum(
            item["quantity"]
            for item in items
            if item["product_id"] == product["product_id"]
        )

        available_stock = product["stock"] - reserved_qty

        if quantity > available_stock:
            print(
                f"  ✗ Only {available_stock} unit(s) of "
                f"'{product['name']}' available. Try again.\n"
            )
            continue

        # Calculate item subtotal
        unit_price = product["selling_price"]
        line_total = round(unit_price * quantity, 2)
        cost_price = product.get("cost_price", 0.0)

        items.append({
            "product_id": product["product_id"],
            "name": product["name"],
            "unit_price": unit_price,
            "quantity": quantity,
            "line_total": line_total,
        })

        subtotal += line_total
        total_cost += cost_price * quantity

        print(f"  ✓ Added {quantity} x {product['name']} = RM{line_total:.2f}\n")

    if not items:
        print("No items added. Sale cancelled.\n")
        return None

    subtotal = round(subtotal, 2)

    # Calculate discount
    discount_rate, discount_amount = calculate_discount(subtotal)
    amount_after_discount = round(subtotal - discount_amount, 2)

    # Calculate the 6% simulated sales tax (applied after discount)
    tax_amount = calculate_tax(amount_after_discount)

    # Calculate the final total
    final_total = round(amount_after_discount + tax_amount, 2)

    # Calculate gross profit (revenue after discount, before tax, minus cost)
    gross_profit = round(amount_after_discount - total_cost, 2)

    sale = {
        "sale_id": _generate_sale_id(sales),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # record current time and date automatically
        "items": items,
        "subtotal": subtotal,
        "discount_rate": discount_rate,
        "discount_amount": discount_amount,
        "tax_amount": tax_amount,
        "total": final_total,
        "gross_profit": gross_profit,
    }

    # Update stock only after the sale is completed
    for item in items:
        product = _find_product(products, item["product_id"])

        if product is not None:
            product["stock"] -= item["quantity"]
            product["units_sold"] = (
                product.get("units_sold", 0) + item["quantity"]
            )

    sales.append(sale)
    generate_receipt(sale)
    return sale


# --------------------------------------------------------------------------
# Display functions
# --------------------------------------------------------------------------

def generate_receipt(sale):
    """Print a formatted receipt for a single sale dict."""
    print("\n" + "=" * 40)
    print("               RECEIPT")
    print("=" * 40)
    print(f"Sale ID:   {sale['sale_id']}")
    print(f"Date/Time: {sale['timestamp']}")
    print("-" * 40)
    print(f"{'Item':<18}{'Qty':>5}{'Unit':>8}{'Total':>9}")
    for item in sale["items"]:
        print(f"{item['name']:<18}{item['quantity']:>5}"
              f"{item['unit_price']:>8.2f}{item['line_total']:>9.2f}")
    print("-" * 40)
    print(f"{'Subtotal:':<31}RM{sale['subtotal']:>7.2f}")
    print(f"{'Discount (' + str(int(sale['discount_rate']*100)) + '%):':<31}"
          f"-RM{sale['discount_amount']:>6.2f}")
    print(f"{'Tax (6%):':<31}RM{sale['tax_amount']:>7.2f}")
    print(f"{'TOTAL:':<31}RM{sale['total']:>7.2f}")
    print("=" * 40)
    print(f"(Internal) Gross Profit: RM{sale['gross_profit']:.2f}")
    print("=" * 40 + "\n")


def display_sales_history(sales):
    """Print a summary list of all completed sales."""
    if not sales:
        print("\nNo sales recorded yet.\n")
        return

    print("\n--- Sales History ---")
    print(f"{'Sale ID':<14}{'Date/Time':<20}{'Items':<8}{'Total':>10}")
    print("-" * 52)
    for sale in sales:
        item_count = sum(i["quantity"] for i in sale["items"])
        print(f"{sale['sale_id']:<14}{sale['timestamp']:<20}"
              f"{item_count:<8}{'RM' + format(sale['total'], '.2f'):>10}")
    print("-" * 52)
    grand_total = round(sum(s["total"] for s in sales), 2)
    print(f"{'TOTAL COLLECTED:':<42}RM{grand_total:.2f}\n")


# --------------------------------------------------------------------------
# Manual test / demo section
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # Sample product list for standalone testing of this module.
    demo_products = [
    {
        "product_id": "P001",
        "name": "Notebook",
        "selling_price": 12.50,
        "cost_price": 8.00,
        "stock": 50,
        "units_sold": 0
    },
    {
        "product_id": "P002",
        "name": "Pen",
        "selling_price": 2.00,
        "cost_price": 1.00,
        "stock": 200,
        "units_sold": 0
    },
    {
        "product_id": "P003",
        "name": "Backpack",
        "selling_price": 89.90,
        "cost_price": 55.00,
        "stock": 10,
        "units_sold": 0
    },
]
    demo_sales = []

    print("=== sales.py standalone demo ===")
    print("Available products:")
    for p in demo_products:
        print(
            f"  {p['product_id']}: {p['name']} - "
            f"RM{p['selling_price']:.2f} "
            f"(stock: {p['stock']})"
        )

    record_sale(demo_products, demo_sales)
    display_sales_history(demo_sales)

    print("Updated stock levels:")
    for p in demo_products:
        print(
            f"  {p['product_id']}: {p['name']} - "
            f"stock={p['stock']}, "
            f"units_sold={p['units_sold']}"
        )