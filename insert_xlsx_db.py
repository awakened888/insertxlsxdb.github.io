import pandas as pd
import mysql.connector

# create a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="database1"
)

# read data from the Excel file into a Pandas DataFrame
df = pd.read_excel("table1.xlsx")

# insert the data into the MySQL database
cursor = conn.cursor()
for row in df.itertuples():
    cursor.execute("""
        INSERT INTO schema1.table1 (id, employeeid, date_1, date_2, name, time_in, time_out, time_total)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (row.id, row.employeeid, row.date_1, row.date_2, row.name, row.time_in, row.time_out, row.time_total))
conn.commit()

# close the database connection
conn.close()
