
import mysql.connector

connection = None
cursor = None

try:
    # 1. Connect Python to MySQL
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_MYSQL_PASSWORD",
        database="company_db"
    )

    print("Connected to MySQL successfully!")

    # 2. Create a cursor to execute SQL
    cursor = connection.cursor()

    # 3. Insert multiple orders
    insert_query = """
        INSERT INTO orders (order_id, customer_name, amount, status)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            customer_name = VALUES(customer_name),
            amount = VALUES(amount),
            status = VALUES(status)
    """

    orders = [
        (101, "Amit", 2500.00, "Completed"),
        (102, "Priya", 1800.00, "Pending"),
        (103, "Rahul", 3200.00, "Completed")
    ]

    cursor.executemany(insert_query, orders)

    # 4. Save the transaction
    connection.commit()
    print("Orders inserted successfully!")

    # 5. Read data from MySQL
    cursor.execute("""
        SELECT order_id, customer_name, amount, status
        FROM orders
        ORDER BY order_id
    """)

    rows = cursor.fetchall()

    # 6. Display the retrieved records
    for row in rows:
        print(row)

except mysql.connector.Error as error:
    print("Database error:", error)

    # Undo uncommitted changes if an error occurs
    if connection is not None and connection.is_connected():
        connection.rollback()

finally:
    # 7. Release resources safely
    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()
        print("Database connection closed.")
