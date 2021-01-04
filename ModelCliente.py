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
        print("Cliente cadastrado com sucesso!")

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


    def deleta_cliente(self,id):
        quary = (f'DELETE FROM Cliente WHERE id = {id}')
        self.cursor.execute(quary)
        self.cnx.commit()
        print("Cliente deletado com sucesso")

    def altera_cliente(self,id):
        quary = (f"SELECT id, nome, sobrenome, telefone, endereco, status from Cliente WHERE id = {id}")
        self.cursor.execute(quary)
        for registro in self.cursor:
            print(f'Id: {registro[0]} | Nome: {registro[1]} {registro[2]} | '
                  f'Telefone: {registro[3]} | Endereço: {registro[4]} | Status: {registro[5]}')
        escolha = int(input("qual informação deseja alterar?\n"
                            "(1)Nome | (2)Sobrenome | (3)Telefone | (4)Endereço\n"))
        if (escolha == 1):
            update = input("Digite o novo nome:\n")
            quary = (f'update Cliente set nome = "{update}" where id = {id}')
            self.cursor.execute(quary)
            self.cnx.commit()
            print("Alteração realizada!")
        elif (escolha == 2):
            update = input("Digite o novo sobrenome:\n")
            quary = (f'update Cliente set sobrenome = "{update}" where id = {id}')
            self.cursor.execute(quary)
            self.cnx.commit()
            print("Alteração realizada!")
        elif (escolha == 3):
            update = input("Digite o novo telefone:\n")
            quary = (f'update Cliente set telefone = "{update}" where id = {id}')
            self.cursor.execute(quary)
            self.cnx.commit()
            print("Alteração realizada!")
        elif (escolha == 4):
            update = input("Digite o novo endereço:\n")
            quary = (f'update Cliente set endereco = "{update}" where id = {id}')
            self.cursor.execute(quary)
            self.cnx.commit()
            print("Alteração realizada!")
        else:
            print('Escolha invalida! Tente novamente.')





