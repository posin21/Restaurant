import pyodbc


SERVER = 'localhost'
DATABASE = 'RestaurantDB'
DRIVER = 'ODBC Driver 17 for SQL Server'

conn = pyodbc.connect(
    f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;"
)

cursor = conn.cursor()
try:
    cursor.execute("INSERT INTO Inventory (itemID, name, quantity, supplierID1, supplierID2, lastRestockDate)"
    " VALUES (?, ?, ?, ?, ?, ?)", 
                   (4, 'sss', 1, 2, 3, '2025-03-29 12:00:00'))
    conn.commit()
except pyodbc.IntegrityError as e:
    print("IntegrityError:", e)
