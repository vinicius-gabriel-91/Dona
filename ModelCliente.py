class Cliente:
    def __init__(self,id, nome, endereco, telefone):
        self.__id = id
        self._nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.status = True

    def __str__(self):
        return f'{self.id} - {self._nome} - {self.endereco} - {self.telefone} - {self.status}'

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

    def altera_endereco(self, endereco):
        self.endereco = endereco

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




