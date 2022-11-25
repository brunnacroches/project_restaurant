from restaurant.interfaces.cook import OrganizeCooksInterface
from restaurant.interfaces.clean import HygienicFoodInterface, WashDishesInterface

class KitcherHelpersGeral(OrganizeCooksInterface):
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

    def organize_equipment(self) -> int:
        print('Turn on the equipment before starting the opening of the restaurant')


    def organize_utensils(self) -> int:
        print('Turn on the utensils before opening the restaurant and after')

    def organize_plates(self) -> int:
       print('Leave the dishes prepared in a separate place to receive the dishes already used')

class KitcherHelpersSanitation(HygienicFoodInterface):
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

    def hygienic_fruits_food(self) -> int:
        print('After sanitizing the fruits, talk in an airy place')


    def hygienic_vegetables_food(self) -> int:
        print('After cleaning the vegetables, dry them well and store them in the fridge')

    def hygienic_meats_food(self) -> int:
       print('Sanitize all meats before going in the fridge and after defrosting')

class KitcherHelpersWashDishes(WashDishesInterface):
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

    def wash_dishes(self) -> int:
        print('Wash dishes with detergent and warm water')


    def wash_glasses(self) -> int:
        print('Wash glasses separately from dishes')

    def wash_cutlery(self) -> int:
       print('Decontaminate cutlery before washing it')
