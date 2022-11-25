from restaurant.interfaces.orders import OrdersInterface, ServerCustomersInterface, ServerPhoneInterface, ServerSuppliersInterface, SchedulesInterface

class RecepcionistOrders(OrdersInterface):
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

    def server_food(self) -> int:
        print('Server food next')

    def server_drinks(self) -> int:
        print('Server drinks first')

    def collect_platters(self) -> int:
       print('Take annotations')

class RecepcionistCustomer(ServerCustomersInterface):
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

    def receive_customers(self) -> int:
        print('Welcome a customer to the table explaining the menu')

    def check_table_availability(self) -> int:
        print('Check table reservations and availability')

    def organize_waiting_table(self) -> int:
       print('Leave the table ready')

class RecepcionistSuppliers(ServerSuppliersInterface):
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

    def call_suppliers(self) -> int:
        print('Call customers confirming reservation within 3 days')

    def budget(self) -> int:
        print('Receive quotes from suppliers a week before products run out')

    def schedule_delivery(self) -> int:
       print('Take notes of orders and send the report by the end of the day')

class RecepcionistPhone(ServerPhoneInterface):
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

    def server_client_phone(self) -> int:
        print('Confirm reservation')


class RecepcionistSchedules(SchedulesInterface):
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

    def make_appointments(self) -> int:
        print('Make notes about')

