import pyodbc

# Open a connection to the database server.
myConnection = pyodbc.connect(
    server="cisdbss.pcc.edu",
    database="IMDB",
    user="275student",
    password="275student",
    driver="{ODBC Driver 17 for SQL Server}"
)

# Create a cursor
cursor = myConnection.cursor()

# Define a SQL command
sql = """
SELECT TOP 50 *
FROM title_basics;
"""

# Execute the SQL command.
cursor.execute(sql)

# Fetch the results from the cursor
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
myConnection.close()