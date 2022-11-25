from abc import ABC, abstractmethod
 
# tudo sobre COZINHAR
class CookInterface(ABC):

  @abstractmethod
  def prepare_food(self) -> int: pass

  @abstractmethod
  def prepare_hot_food(self) -> int: pass

  @abstractmethod
  def prepare_cold_food(self) -> int: pass

  @abstractmethod
  def prepare_sweet_food(self) -> int: pass


class OrganizeCooksInterface(ABC):
  @abstractmethod
  def organize_equipment(self) -> int: pass

  @abstractmethod
  def organize_utensils(self) -> int: pass

  @abstractmethod
  def organize_plates(self) -> int: pass


class CookCutInterface(ABC):

  @abstractmethod
  def cut_vegetables(self) -> int: pass

  @abstractmethod
  def cut_meat(self) -> int: pass

  @abstractmethod
  def cut_fruits(self) -> int: pass