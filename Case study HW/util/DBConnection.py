# In util/DBConnection.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pyodbc

from util.PropertyUtil import PropertyUtil

class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        if DBConnection.connection is None:
           try:
               connection_string = PropertyUtil.getPropertyString()
               DBConnection.connection = pyodbc.connect(connection_string)
               print("Connected Successfully")
           except pyodbc.Error as e:
             print(f"Connection failed: {e}")
        else:
          print("Connection already established")

        return DBConnection.connection
