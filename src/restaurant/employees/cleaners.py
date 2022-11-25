from restaurant.interfaces.clean import ClearFurnitureInterface, ClearRestaurantInterface

class CleanersDetails(ClearFurnitureInterface):
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

    def clear_forniture_external(self) -> int:
        print('Clean outdoor furniture one day and one day not')


    def clear_forniture_internal(self) -> int:
        print('Clean the inside of the restaurant every 4 hours every day')

    def clear_windows(self) -> int:
       print('clean the windows once a week')


class CleanersGeral(ClearRestaurantInterface):
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

    def clear_floor(self) -> int:
        print('Clean the floor three times a day')


    def wash_towels(self) -> int:
        print('Wash towels at the end of the day')

    def clear_ceiling(self) -> int:
       print('Clean the ceiling once every 15 days')