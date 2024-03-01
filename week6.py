from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

# define the MealBuilder abstract base class 
# creating different parts of the meal
class MealBuilder(ABC):
  """
  The MealBuilder interface specifies methods for creating the different parts of the Meal objects.
  """
  @property 
  @abstractmethod
  def meal(self) -> None:
    pass

  @abstractmethod
  def prepare_starter(self) -> None:
    pass

  @abstractmethod
  def prepare_main_course(self) -> None:
    pass

  @abstractmethod
  def prepare_dessert(self) -> None:
    pass

# creating concrete class - ItalianMealBuilder which implements the MealBuilder interface
# building a specific type of meal 

class ItalianMealBuilder(MealBuilder):
  """
  Concrete Meal Builders follow the MealBuilder interface and provide specific implementations of the building steps for different types of meals.
  """

  def __init__(self) -> None:
    self.reset()

  def reset(self) -> None:
    self._meal = ItalianMeal()

  @property
  def meal(self) -> ItalianMeal:
      meal = self._meal
      self.reset()
      return meal

  def prepare_starter(self) -> None:
        self._meal.add("Bruschetta")

  def prepare_main_course(self) -> None:
        self._meal.add("Spaghetti Carbonara")

  def prepare_dessert(self) -> None:
        self._meal.add("Tiramisu")

# create the product class 
class ItalianMeal():
    """
    Concrete products created by the corresponding Concrete Builders.
    """

    def __init__(self) -> None:
        self.parts = []
 
 
    def add(self, part: Any) -> None:
        self.parts.append(part)
 
 
    def list_parts(self) -> None:
        print(f"Meal components: {', '.join(self.parts)}", end="")

#creating the CulinaryDirector - executing the building steps in a specific sequence 
class CulinaryDirector:
    """
    The CulinaryDirector is responsible for executing the building steps in a particular sequence. It is crucial when preparing meals according to specific recipes or configurations.
    """

    def __init__(self) -> None:
        self._builder = None
 
    @property
    def builder(self) -> MealBuilder:
        return self._builder
 
    @builder.setter
    def builder(self, builder: MealBuilder) -> None:
        self._builder = builder
 
    def prepare_basic_meal(self) -> None:
        self.builder.prepare_main_course()
 
    def prepare_full_meal(self) -> None:
        self.builder.prepare_starter()
        self.builder.prepare_main_course()
        self.builder.prepare_dessert()
# creating builder pattern in a client code scenario
# includes a creating a director, setting a builder, and initiating the building process to create differnt types of meals 

if __name__ == "__main__":
    director = CulinaryDirector()
    builder = ItalianMealBuilder()
    director.builder = builder
 
 
    print("Basic meal: ")
    director.prepare_basic_meal()
    builder.meal.list_parts()
 
 
    print("\n")
 
 
    print("Full Italian meal: ")
    director.prepare_full_meal()
    builder.meal.list_parts()
 
 
    print("\n")

# demonstrating usage without the CulinaryDirector
    print("Custom meal: ")
    builder.prepare_starter()
    builder.prepare_dessert()  # Maybe you only want a starter and dessert.
    builder.meal.list_parts()
