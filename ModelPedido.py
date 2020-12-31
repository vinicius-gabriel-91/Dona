class Pedido:
    def __init__(self,id, cliente, descricao):
        self.__id = id
        self._cliente = cliente
        self.descricao = descricao
        self.status = False

    def __str__(self):
        return f'{self.id} - {self.cliente} - {self.descricao} - {self.status}'

# --------------------PROPRIEDADES---------------------------------------------------------

    @property
    def id(self):
        return self.__id

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def altera_cliente(self, cliente):
        self._cliente = cliente

# -----------------------METODOS-------------------------------------------------------------

    def altera_pedido(self, descricao):
        self.descricao = descricao

    def altera_status(self):
        if (self.status):
            status = "Concluido"
        else:
            status = "Em andamento"

        resposta = input(f'O pedido: {self.id}\n'
              f'Atualmente esta como: {status}\n'
              f'Deseja altera-lo?: S ou N\n')
        resposta = resposta.title()

        if (resposta == 'S'):
            resposta = int(input('Como deseja marcar o pedido?: (1)Concluido (2)Em andamento\n'))
        if (resposta == 1):
            self.status = True
            print(f'Pedido {self.id} marcado como Conluido')
        elif (resposta == 2):
            self.status = False
            print(f'Pedido {self.id} marcado como Em andamente')



pedido = Pedido(1,'Vinicius','torta')
pedido.altera_status()
print(pedido)
