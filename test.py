from flask import Flask, render_template, jsonify
import pyodbc

app = Flask(__name__)
SERVER = 'localhost'
DATABASE = 'RestaurantDB'
DRIVER = 'ODBC Driver 17 for SQL Server'

conn = pyodbc.connect(
    f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;"
)

@app.route('/')
def home():
    return render_template('index.html')


#Supplier
@app.route('/supplier')
def supplier():
    return render_template('supplier.html')

@app.route('/get-supplier', methods=['GET'])
def get_suppliers():
    cursor = conn.cursor()
    cursor.execute("SELECT supplierID, name, contactInfo FROM Supplier")
    rows = cursor.fetchall()

    python_list = [{"supplierID": row[0], "name": row[1], "contactInfo": row[2]} for row in rows]

    return jsonify(python_list)

#Inventory
@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

@app.route('/get-inventory', methods=['GET'])
def get_inventory():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Inventory")
    rows = cursor.fetchall()

    python_list = [{"itemID": row[0], "name": row[1], "quantity": row[2], "supplierID1": row[3], "supplierID2": row[4], "lastRestockDate": row[5]} for row in rows]

    return jsonify(python_list)



@app.route('/tables')
def tables():
    return render_template('tables.html')

if __name__ == '__main__':
    app.run(debug=True)