import pyodbc  # installed by pip

print("Before open connection")
print()

conn = pyodbc.connect(Trusted_Connection='yes', driver='{SQL Server}', server='LAPTOP-A8BTI830', database='CarDB')

cursor = conn.cursor()
cursor.execute("SELECT * FROM Car")

row = cursor.fetchone()  # fetch the first row
while row:
    print(str(row.ID) + " : " + row.Model + " : " + str(row.MaxSpeed) + " km/t")
    row = cursor.fetchone()  # fetch the next row

conn.close()

print()
print("After closing connection")