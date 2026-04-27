import sqlite3

# Connect database
conn = sqlite3.connect("restaurant.db")
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    item TEXT,
    quantity INTEGER,
    price INTEGER
)
""")
conn.commit()

# Add Order
def add_order():
    name = input("Enter customer name: ")
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = int(input("Enter price: "))

    cur.execute("INSERT INTO orders (name, item, quantity, price) VALUES (?, ?, ?, ?)",
                (name, item, quantity, price))
    conn.commit()
    print("Order Added Successfully!\n")

# View Orders
def view_orders():
    cur.execute("SELECT * FROM orders")
    rows = cur.fetchall()

    print("\nOrders List:")
    print("-"*50)
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Item: {row[2]} | Qty: {row[3]} | Price: {row[4]}")
    print("-"*50 + "\n")

# Update Order
def update_order():
    order_id = int(input("Enter Order ID to update: "))

    cur.execute("SELECT * FROM orders WHERE id=?", (order_id,))
    row = cur.fetchone()

    if row:
        print("Enter new details:")
        name = input("New customer name: ")
        item = input("New item name: ")
        quantity = int(input("New quantity: "))
        price = int(input("New price: "))

        cur.execute("""
        UPDATE orders 
        SET name=?, item=?, quantity=?, price=? 
        WHERE id=?
        """, (name, item, quantity, price, order_id))

        conn.commit()
        print("Order Updated Successfully!\n")
    else:
        print("Order ID not found!\n")

# Delete Order
def delete_order():
    order_id = int(input("Enter Order ID to delete: "))

    cur.execute("SELECT * FROM orders WHERE id=?", (order_id,))
    row = cur.fetchone()

    if row:
        cur.execute("DELETE FROM orders WHERE id=?", (order_id,))
        conn.commit()
        print("Order Deleted Successfully!\n")
    else:
        print("Order ID not found!\n")

# Total Bill
def total_bill():
    cur.execute("SELECT SUM(quantity * price) FROM orders")
    total = cur.fetchone()[0]

    if total:
        print(f"\nTotal Bill: Rs.{total}\n")
    else:
        print("\nNo orders found!\n")

# Menu
while True:
    print("===== Restaurant Order System =====")
    print("1. Add Order")
    print("2. View Orders")
    print("3. Update Order")
    print("4. Delete Order")
    print("5. Total Bill")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_order()
    elif choice == '2':
        view_orders()
    elif choice == '3':
        update_order()
    elif choice == '4':
        delete_order()
    elif choice == '5':
        total_bill()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice!\n")

conn.close()
