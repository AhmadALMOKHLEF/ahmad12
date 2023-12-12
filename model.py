import pyodbc

class RealEstateModel:
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={SQL Server};'
                                   'SERVER=ADMIN-PC\SQLEXPRESS;'
                                   'DATABASE=Real Estate Agency Card;'
                                   'UID=abcd;'
                                   'PWD=abcd')
        self.cursor = self.conn.cursor()

    def get_apartments(self):
        self.cursor.execute("SELECT * FROM Apartments")
        return self.cursor.fetchall()

    def get_clients(self):
        self.cursor.execute("SELECT * FROM Clients")
        return self.cursor.fetchall()

    def get_applications(self):
        self.cursor.execute("SELECT * FROM Applications")
        return self.cursor.fetchall()

    # Add other methods for CRUD operations as needed
