import mysql.connector
class Pedido:
    def __init__(self):

        config = {
            'user': 'admin',
            'password': 'password',
            'host': '127.0.0.1',
            'database': 'Dona',
            'raise_on_warnings': True
        }

        self.cnx = mysql.connector.connect(**config)
        self.cursor = self.cnx.cursor()

