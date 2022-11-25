from abc import ABC, abstractmethod

#  tudo sobre PEDIDOS
# waiters
# musicans
# recepcionista

class OrdersInterface(ABC): 

  @abstractmethod
  def server_food(self) -> int: pass

  @abstractmethod
  def server_drinks(self) -> int: pass

  @abstractmethod
  def collect_platters(self) -> int: pass

  @abstractmethod
  def prepare_meals_table(self) -> int: pass

  @abstractmethod
  def compose_music(self) -> int: pass

  @abstractmethod
  def interpret_music(self) -> int: pass

  @abstractmethod
  def rehearse_music(self) -> int: pass

  @abstractmethod
  def create_music(self) -> int: pass

# atender clientes
class ServerCustomersInterface(ABC):
  @abstractmethod
  def receive_customers(self) -> int: pass

  @abstractmethod
  def check_table_availability(self) -> int: pass

  @abstractmethod
  def organize_waiting_table(self) -> int: pass

# atender fornecedores
class ServerSuppliersInterface(ABC):

  @abstractmethod
  def call_suppliers(self) -> int: pass

  @abstractmethod
  def budget(self) -> int: pass

  @abstractmethod
  def schedule_delivery(self) -> int: pass

# atender telefone
class ServerPhoneInterface(ABC):

  @abstractmethod
  def server_client_phone(self) -> int: pass

# agendamentos
class SchedulesInterface(ABC):

  @abstractmethod
  def make_appointments(self) -> int: pass

  @abstractmethod
  def confirm_appointments(self) -> int: pass
