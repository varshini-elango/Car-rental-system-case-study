# In util/PropertyUtil.py

class PropertyUtil:
    @staticmethod
    def getPropertyString():
     
        server_name = r"DESKTOP-2S6KAQD\SQLEXPRESS"
        database_name = "casestudy"
        trusted_connection = "yes"
        return f"Driver={{SQL Server}};Server={server_name};Database={database_name};Trusted_Connection={trusted_connection};"
       
