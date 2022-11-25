from abc import ABC, abstractmethod

# pedidos
class RequestsInterface(ABC):
  @abstractmethod
  def taking_orders(self) -> int: pass

  @abstractmethod
  def organizing_orders(self) -> int: pass

  @abstractmethod
  def delivery_menu(self) -> int: pass

