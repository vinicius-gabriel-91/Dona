import mysql.connector

class Cliente:
    __id = None
    _nome = None
    endereco = None
    telefone = None
    status = None
    _sobrenome = None

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

    def __str__(self):
        return f'{self.id} - {self._nome} - {self._sobrenome} - {self.endereco} - {self.telefone} - {self.status}'

    # --------------------PROPRIEDADES---------------------------------------------------------

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    # -----------------------METODOS-------------------------------------------------------------

    def inclui_cliente(self, nome, sobrenome, telefone=000000000, endereco = 'null', status = False):
        self.nome = nome
        self._sobrenome = sobrenome
        self.endereco = endereco
        self.telefone = telefone
        self.status = status

        add_cliente = (f'INSERT INTO Cliente '
                       '(id, nome, sobrenome, telefone, endereco, status) '
                       f'VALUES (null, "{nome}", "{sobrenome}", "{telefone}", "{endereco}", {status})')

        self.cursor.execute(add_cliente)
        self.cnx.commit()

    def get_list(self):
        quary = ("SELECT * FROM Cliente")
        self.cursor.execute(quary)

        for registro in self.cursor:
            print(f'Id: {registro[0]} | Nome: {registro[1]} {registro[2]} | '
                  f'Endereço: {registro[3]} | Telefone: {registro[4]} | Status: {registro[5]}')


    def get_info(self,telefone):
        quary = (f"SELECT id, nome, sobrenome, telefone, endereco, status from Cliente WHERE telefone = '{telefone}'")
        self.cursor.execute(quary)

        for registro in self.cursor:
            print(f'Id: {registro[0]} | Nome: {registro[1]} {registro[2]} | '
                  f'Telefone: {registro[3]} | Endereço: {registro[4]} | Status: {registro[5]}')

        row = self.cursor.fetchone()
        if (row == None):
            print("Registro não encontrado! Tente novamente.")

    def altera_endereco(self, endereco):
        self.endereco = endereco

    def altera_telefone(self, telefone):
        self.telefone = telefone

    def altera_status(self):
        if (self.status):
            status = "Ativo"
        else:
            status = "Desativado"

        resposta = input(f'O cliente: {self.id}\n'
                         f'Atualmente esta como: {status}\n'
                         f'Deseja altera-lo?: S ou N\n')
        resposta = resposta.title()

        if (resposta == 'S'):
            resposta = int(input('Como deseja marcar o cliente?: (1)Ativo (2)Desativado\n'))
        if (resposta == 1):
            self.status = True
            print(f'Cliente {self.id} marcado como Ativo')
        elif (resposta == 2):
            self.status = False
            print(f'Pedido {self.id} marcado como Desativado')

