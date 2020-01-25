import pyodbc
from .abs_facade import AbsFacade
from . import CONNSTR, QUERY

# here, we implement the Facade and connection string settings
class GetEmployeesFacade(AbsFacade):
    # method implemented - this defines logic for getting employees records
    def get_employees(self):
        connection = pyodbc.connect(CONNSTR)
        cursor = connection.cursor()
        cursor.execute(QUERY)
        # the loop can be moved
        for row in cursor:
            print(row.FirstName, row.LastName)

        connection.commit()
        connection.close()

# we don't need to change this code if the CONNSTR or the Query changes
