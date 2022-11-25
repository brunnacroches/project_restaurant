from restaurant.interfaces.cook import CookInterface, CookCutInterface, OrganizeCooksInterface

class CooksDetails(CookInterface):
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

    def prepare_food(self) -> int:
        print('Prepare the food as soon as you receive the order')


    def prepare_hot_food(self) -> int:
        print('Prepare hot dishes before preparing cold dishes')

    def prepare_sweet_food(self) -> int:
       print('Make the sweet dishes after the main entrance')


class CookCutGeral(CookCutInterface):
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

    def cut_vegetables(self) -> int:
        print('Cut the vegetables after immediate order to keep them fresh')


    def cut_meat(self) -> int:
        print('Defrost the meat completely before cutting it')

    def cut_fruits(self) -> int:
       print('Store the fruits in the refrigerator half an hour before cutting')