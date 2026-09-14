# Small Business Inventory and Sales System (SBISS)

## 1. Introduction

The Small Business Inventory and Sales System (SBISS) is a Python-based program used to manage products, inventory, sales transactions, and business reports.

The system allows the user to:

* Add new products
* Display all products
* Search for products
* Update product information
* Delete products
* Restock products
* Record sales transactions
* Display sales history
* Generate business reports
* Save product and sales data

---

## 2. Requirements

Before running the program, make sure that:

* Python 3 is installed on the computer.
* All Python files are saved in the same project folder.
* The program is run using `main.py`.

No additional Python libraries need to be installed because the program only uses standard Python libraries such as `json`, `os`, `uuid`, and `datetime`.

---

## 3. Project Structure

The project folder should be arranged as follows:

```text
SBISS/
│
├── main.py
├── inventory.py
├── sales.py
├── reports.py
├── utils.py
│
└── data/
    ├── products.json
    └── sales.json
```

### File Description

* `main.py` – Main program used to start and control the system.
* `inventory.py` – Handles product and inventory functions.
* `sales.py` – Handles sales transactions, calculations, and receipts.
* `reports.py` – Generates inventory and sales reports.
* `utils.py` – Handles loading and saving JSON data.
* `products.json` – Stores product information.
* `sales.json` – Stores sales transaction records.

The `data` folder will be created automatically if it does not already exist.

---

## 4. How to Run the Program

### Step 1: Open the Project Folder

Open the `SBISS` project folder using Visual Studio Code or another Python development environment.

In Visual Studio Code:

```text
File → Open Folder → Select the SBISS folder
```

---

### Step 2: Open the Terminal

In Visual Studio Code, select:

```text
Terminal → New Terminal
```

Make sure the terminal is currently inside the project folder.

For example:

```text
C:\Users\User\Documents\SBISS>
```

---

### Step 3: Run the Main Program

Enter the following command in the terminal:

```bash
python main.py
```

If the `python` command does not work on Windows, try:

```bash
py main.py
```

Press **Enter** to start the program.

---

## 5. Main Menu

After starting the program, the following menu will be displayed:

```text
==================================================
 SMALL BUSINESS INVENTORY AND SALES SYSTEM
==================================================
1. Add a new product
2. Display all products
3. Search for a product
4. Update product information
5. Delete a product
6. Restock a product
7. Record a sale
8. Display sales history
9. Generate reports
10. Save data
11. Exit
==================================================
Enter your choice (1-11):
```

Enter a number from `1` to `11` to select an option.

---

## 6. Example: Adding a Product

Select:

```text
1. Add a new product
```

Example input:

```text
Enter Product ID: P001
Enter Product Name: Wireless Mouse
Enter Category: Accessories
Enter Cost Price (RM): 25
Enter Selling Price (RM): 39.90
Enter Initial Stock Quantity: 10
```

The program will display:

```text
Success: Product P001 added.
```

The product information will then be saved into the product data file.

---

## 7. Example: Recording a Sale

Select:

```text
7. Record a sale
```

Enter the Product ID:

```text
Product ID (or 'done' to finish): P001
```

Enter the quantity:

```text
Quantity for 'Wireless Mouse': 2
```

After adding all products, enter:

```text
done
```

The system will calculate the:

* Subtotal
* Discount
* Sales tax
* Final total
* Gross profit

It will also automatically reduce the product stock and increase the number of units sold.

A receipt will be displayed after the transaction is completed.

---

## 8. Saving Data

Product and sales information is stored in JSON files.

The files are:

```text
data/products.json
data/sales.json
```

The program automatically saves data after important operations such as:

* Adding a product
* Updating a product
* Deleting a product
* Restocking a product
* Recording a sale

The user can also manually save the data by selecting:

```text
10. Save data
```

---

## 9. Generating Reports

Select:

```text
9. Generate reports
```

The system can generate several business reports, including:

* Inventory Summary
* Low Stock Report
* Out of Stock Report
* Sales Summary
* Gross Profit Summary
* Best Selling Product
* Highest Value Transaction
* Category Summary

For the Low Stock Report, the user will be asked to enter a stock threshold.

Example:

```text
Enter stock threshold: 5
```

Products with stock below the selected threshold will then be displayed.

---

## 10. Exiting the Program

To exit the program, select:

```text
11. Exit
```

The program will save the current data before closing.

The following message will be displayed:

```text
Data saved successfully.
Thank you for using SBISS. Goodbye!
```

---

## Important Note

The program should always be started from:

```bash
python main.py
```

Do not run all Python files separately.

`main.py` imports and connects the functions from `inventory.py`, `sales.py`, `reports.py`, and `utils.py`, allowing the complete system to work together.
