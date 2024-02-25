import sqlite3


data = sqlite3.connect('MedStocks.db')
table = 'stocks'

# create_table = """ CREATE TABLE IF NOT EXISTS projects (
  
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         name text NOT NULL,
#                         begin_date text,
#                         end_date text
                        
#                     ); """
                                    
# data.execute(f"create table {table} (id INTEGER PRIMARY KEY AUTOINCREMENT,\
#                                     name VARCHAR(25),\
#                                     price FLOAT,\
#                                     quantity INT\
#                                     )\
#                                     ")

data.execute(f"INSERT INTO  {table}(name, price, quantity)\
              VALUES ( 'hmd', 0.0, 99999)"
            )

data.commit()

cursor = data.execute( f"SELECT * FROM {table}")
print(cursor.fetchall())
