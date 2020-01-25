import pyodbc

CONNSTR = 'DRIVER={SQL Server};SERVER=YOUR_SERVER;DATABASE=YOUR_DATABASE;UID=YOUR_USER;PWD=YOUR_PASSWORD'

def get_employees():
    connection = pyodbc.connect(CONNSTR)
    query = 'SELECT DISTINCT TOP 5 FirstName, LastName FROM Person.Person ORDER BY LastName, FirstName;'
    cursor = connection.cursor()
    cursor.execute(query)
    for row in cursor:
        print(row.FirstName, row.LastName)

    connection.commit()
    connection.close()

# calling the method
get_employees()
