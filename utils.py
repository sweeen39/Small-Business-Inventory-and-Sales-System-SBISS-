import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

PRODUCTS_FILE = os.path.join(DATA_DIR, "products.json")
SALES_FILE = os.path.join(DATA_DIR, "sales.json")

def load_data():
    """Load product and sales data from JSON files."""
    products = []
    sales = []

    # Create data folder if it does not exist
    os.makedirs(DATA_DIR, exist_ok=True)

    # Load products
    try:
        with open(PRODUCTS_FILE, "r") as file:
            products = json.load(file)

            # If JSON is not a list, use an empty list
            if not isinstance(products, list):
                products = []

    except (FileNotFoundError, json.JSONDecodeError):
        products = []

    # Load sales
    try:
        with open(SALES_FILE, "r") as file:
            sales = json.load(file)

            # If JSON is not a list, use an empty list
            if not isinstance(sales, list):
                sales = []

    except (FileNotFoundError, json.JSONDecodeError):
        sales = []

    return products, sales

def save_data(products, sales):
    """Save product and sales data to JSON files."""
    # Create data folder if it does not exist
    os.makedirs(DATA_DIR, exist_ok=True)

    # Save products
    with open(PRODUCTS_FILE, "w") as file:
        json.dump(products, file, indent=4)

    # Save sales
    with open(SALES_FILE, "w") as file:
        json.dump(sales, file, indent=4)

def get_positive_float(message):
    """Get a positive floating-point number from the user."""
    while True:
        try:
            value = float(input(message))

            if value > 0:
                return value
            else:
                print("please enter a positive number")

        except ValueError:
            print("Invalid input. Please enter a number")

def get_non_negative_integer(message):
    """Get a non-negative integer from the user."""
    while True:
        try:
            value = int(input(message))

            if value >= 0:
                return value
            else:
                print("Please enter 0 or a positive number.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

def find_product(products, product_id):
    """Find and return a product by its product ID."""
    for product in products:
        if product.get("product_id", "").lower() == product_id.lower():
            return product

    return None