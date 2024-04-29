import sqlite3, csv

con = sqlite3.connect("my_database.db")
cur = con.cursor()

# создание таблиц
# cur.execute("CREATE TABLE customers (name, address);")
# cur.execute("CREATE TABLE products (product, price, quantity);")
# cur.execute("CREATE TABLE sales (customer, date, products, summ);")

file1 = open('customers.csv')
file2 = open('products.csv')
file3 = open('sales.csv')

contents1 = csv.reader(file1)
contents2 = csv.reader(file2)
contents3 = csv.reader(file3)

# # расположение данных в таблицах

# insert_records = "INSERT INTO customers (name, address) VALUES(?, ?)"
# cur.executemany(insert_records, contents1)

# insert_records = "INSERT INTO products (product, price, quantity) VALUES(?, ?, ?)"
# cur.executemany(insert_records, contents2)

# insert_records = "INSERT INTO sales (customer, date, products, summ) VALUES(?, ?, ?, ?)"
# cur.executemany(insert_records, contents3)

# установление связей между таблицами
cur.execute('SELECT customers.name FROM customers JOIN sales ON (customers.name = sales.customer)')
cur.execute('SELECT sales.products FROM sales JOIN products ON (sales.products = products.product)')
cur.execute('SELECT sales.summ FROM sales JOIN products ON (sales.summ = products.price)')

# запросы
# select_all = "SELECT * FROM sales WHERE sales.products = 'Banana, Tomato, Corn'"
# rows = cur.execute(select_all).fetchall()

select_all = "SELECT * FROM customers WHERE customers.name = 'Ed Vasser' OR customers.name = 'Matias Limb'"
rows = cur.execute(select_all).fetchall()

# select_all = "SELECT * FROM sales, products WHERE sales.summ = products.price"
# rows = cur.execute(select_all).fetchall()

# select_all = 'SELECT * FROM sales'
# rows = cur.execute(select_all).fetchall()

for r in rows:
    print(r)

con.commit()
con.close()
