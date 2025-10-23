from collections import defaultdict

warehouses = defaultdict(lambda: defaultdict(dict))

def displayingproducts(warehouses):
    if not warehouses:
        print("Inventory is empty!")
        return
    for wh_name, categories in warehouses.items():
        print("Warehouse:", wh_name)
        for cat_name, products in categories.items():
            print("  Category:", cat_name)
            for prod_name, qty in products.items():
                print("    Product:", prod_name, "=", qty)

def addproduct(w, c, p, qty):
    warehouses[w][c][p] = qty
    print(f"Product added successfully!")

def update_quantity(w, c, p, new_qty):
    if w in warehouses and c in warehouses[w] and p in warehouses[w][c]:
        warehouses[w][c][p] = new_qty
        print("Quantity updated!")
    else:
        print("Product not found!")

def rename_warehouse(old_w, new_w):
    if old_w in warehouses:
        warehouses[new_w] = warehouses.pop(old_w)
        print("Warehouse renamed!")
    else:
        print("Warehouse not found!")

def rename_category(w, old_c, new_c):
    if w in warehouses and old_c in warehouses[w]:
        warehouses[w][new_c] = warehouses[w].pop(old_c)
        print("Category renamed!")
    else:
        print("Category not found!")

def rename_product(w, c, old_p, new_p):
    if w in warehouses and c in warehouses[w] and old_p in warehouses[w][c]:
        warehouses[w][c][new_p] = warehouses[w][c].pop(old_p)
        print("Product renamed!")
    else:
        print("Product not found!")

def remove_product(w, c, p):
    if w in warehouses and c in warehouses[w] and p in warehouses[w][c]:
        warehouses[w][c].pop(p)
        print("Product removed!")
        # Remove category if empty
        if not warehouses[w][c]:
            warehouses[w].pop(c)
        # Remove warehouse if empty
        if not warehouses[w]:
            warehouses.pop(w)
    else:
        print("Product not found!")

def low_stock_report(threshold=50):
    print("--- Low Stock Report ---")
    found = False
    for wh_name, categories in warehouses.items():
        for cat_name, products in categories.items():
            for prod_name, qty in products.items():
                if qty < threshold:
                    print(f"{prod_name} in {wh_name}/{cat_name} -> Qty: {qty}")
                    found = True
    if not found:
        print("No low stock items!")

def update_menu(w, c, p):
    if w in warehouses and c in warehouses[w] and p in warehouses[w][c]:
        print("Product found! What do you want to update?")
        print("1] Warehouse Name")
        print("2] Category Name")
        print("3] Product Name")
        print("4] Product Quantity")
        n = input("Enter choice (1-4): ")
        if n == "1":
            new_w = input("Enter new warehouse name: ")
            rename_warehouse(w, new_w)
        elif n == "2":
            new_c = input("Enter new category name: ")
            rename_category(w, c, new_c)
        elif n == "3":
            new_p = input("Enter new product name: ")
            rename_product(w, c, p, new_p)
        elif n == "4":
            new_qty = int(input("Enter new quantity: "))
            update_quantity(w, c, p, new_qty)
        else:
            print("Invalid choice!")
    else:
        print("Product not found!")

# Main loop
while True:
    print("\n--- Inventory Management ---")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Remove Product")
    print("4. View Inventory")
    print("5. Low Stock Report")
    print("6. Exit")

    choice = input("Enter choice: ")

    match choice:
        case "1":
            w = input("Enter warehouse name: ")
            c = input("Enter category name: ")
            p = input("Enter product name: ")
            qty = int(input("Enter quantity: "))
            addproduct(w, c, p, qty)
            displayingproducts(warehouses)
        case "2":
            w = input("Enter warehouse name of product: ")
            c = input("Enter category name of product: ")
            p = input("Enter product name to update: ")
            update_menu(w, c, p)
            displayingproducts(warehouses)
        case "3":
            w = input("Enter warehouse name of product: ")
            c = input("Enter category name of product: ")
            p = input("Enter product name to remove: ")
            remove_product(w, c, p)
            displayingproducts(warehouses)
        case "4":
            displayingproducts(warehouses)
        case "5":
            threshold = int(input("Enter low stock threshold: "))
            low_stock_report(threshold)
        case "6":
            print("Exiting Inventory Management. Goodbye!")
            break
        case _:
            print("Invalid choice, try again.")
