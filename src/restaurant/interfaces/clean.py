from abc import ABC, abstractmethod

# tudo sobre limpeza
# os faxineiros e auxiliar de cozinha

# limpar mobília
class ClearFurnitureInterface(ABC):
  
  @abstractmethod
  def clear_forniture_external(self) -> int: pass

  @abstractmethod
  def clear_forniture_internal(self) -> int: pass

  @abstractmethod
  def clear_windows(self) -> int: pass

  @abstractmethod
  def clear_tables(self) -> int: pass

# limpar comida
class HygienicFoodInterface(ABC):

  @abstractmethod
  def hygienic_fruits_food(self) -> int: pass

  @abstractmethod
  def hygienic_vegetables_food(self) -> int: pass

  @abstractmethod
  def hygienic_meats_food(self) -> int: pass

# limpar os pratos
class WashDishesInterface(ABC):

  @abstractmethod
  def wash_dishes(self) -> int: pass

  @abstractmethod
  def wash_glasses(self) -> int: pass

  @abstractmethod
  def wash_cutlery(self) -> int: pass

# limpar restaurante
class ClearRestaurantInterface(ABC):

  @abstractmethod
  def clear_floor(self) -> int: pass

  @abstractmethod
  def wash_towels(self) -> int: pass

  @abstractmethod
  def clear_ceiling(self) -> int: pass

# limpar cozinha
class ClearKitchenInterface(ABC):

  @abstractmethod
  def clear_stove(self) -> int: pass

  @abstractmethod
  def clear_fridge(self) -> int: pass

  @abstractmethod
  def clear_countertop(self) -> int: pass