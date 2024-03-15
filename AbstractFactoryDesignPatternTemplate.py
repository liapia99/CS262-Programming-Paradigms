from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractFactory(ABC):
  """
  The factory interface declares a set of methods and returns different abstract products related to chairs. 
  These products might include the chair itself, perhaps some accesories, but all of those would be related to a design theme or some kind of ergonomic style.
  """
  @abstractmethod
  def create_chair(self) -> AbstractChair:
    pass 

  @abstractmethod
  def create_accessory(self) -> AbstractAccessory:
    pass
  

class AbstractChair(ABC):
    """
    Base interface for a chair product. By virtue of this all chair variants will implement this interface.
    """  
    @abstractmethod
    def sit_on(self) -> str:
        pass

class AbstractAccessory(ABC):
  """
  Basic interface for a chair accessory, like cushions. 
  """
  @abstractmethod
  def complement(self) -> None:
    pass


class ModernChairFactory(AbstractFactory):
  """
  This is a concrete factory producing a modern type of chairs and their accessories.
  """
  def create_chair(self) -> AbstractChair:
    return ModernChair()

  def create_accessory(self) -> AbstractAccessory: 
    return ModernCushion()

class VictorianChairFactory(AbstractFactory):

  def create_chair(self) -> AbstractChair:
    return VictorianChair()

  def create_accessory(self) -> AbstractAccessory:
    return VictorianCushion()






    
class ModernChair(AbstractChair):
  def sit_on(self) -> str:
    return "Sitting on a modern chair."

class ModernCushion(AbstractAccessory):
  def complement(self) -> str:
    return "Complimenting with a modern cushion."

class VictorianChair(AbstractChair):
  def sit_on(self) -> str:
    return "Sitting on a victorian chair."

class VictorianCushion(AbstractAccessory):
  def complement(self) -> str:
    return "Complimenting with a victorian cushion."


  def client_code(factory: AbstractFactory) -> None:
    """
    This client code works with factories and products only through their abstract types: AbstractFactory, AbstractChair, and AbstractAccessory. 
    This allows any factory or product subclass to be passed to the client code without breaking it. 
    """

    chair = factory.create_chair()
    accessory = factory.create_accessory()

    print(f"{chair.sit_on()}")
    print(f"{accessory.complement()}")

if __name__ == "__main__":
  print("Client: Testing client code with the ModernChairFactory:")
  client_code(ModernChairFactory())
  print("\n")
  print("Client: Testing client code with the VictorianChairFactory:")
  client_code(VictorianChairFactory())

  
