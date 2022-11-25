from restaurant.interfaces.requests import RequestsInterface

class WaitersDetails(RequestsInterface):
    def __init__(self, nome: str, function: int) -> None:
        self.__profissao = 'Cleaners'
        self.__nome = nome
        self.function = function

    def learn_information(self) -> None:
        print(f'''
            Nome: {self.__nome},
            Profissao: {self.__profissao},
            Function: {self.__function}
        ''')

    def taking_orders(self) -> int:
        print('Take customer orders as soon as we receive them')

    def organizing_orders(self) -> int:
        print('Separate long orders from short orders')

    def delivery_menu(self) -> int:
       print('Receive customers by presenting the house menu and the executive dish of the day')
