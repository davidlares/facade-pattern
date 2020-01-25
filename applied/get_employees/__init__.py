PROVIDER = 'sql_server'

# you can change it by generating other module instead of replacing it.
CONNSTR = (
    'DRIVER={SQL Server};'
    'SERVER=YOUR_SERVER;'
    'DATABASE=YOUR_DATABASE;'
    'UID=YOUR_USER;PWD=YOUR_PASSWORD'
)

# you can change it by generating other module instead of replacing it.
QUERY = '''
    SELECT DISTINCT TOP 5 FirstName, LastName
    FROM Person.Person
    ORDER BY LastName, FirstName;
'''
