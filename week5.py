class Government:
  _instance = None

# Initializing the object with country, capital and leader
  def __init__(self, country, capital, leader):
    self.country = country
    self.capital = capital 
    self.leader = leader

# government is an instance 
# country, capital, leader are strings 

# defining the class method so that only one instance of governrment class is created 
  @classmethod 
  def get_instance(cls, country, capital, leader):
    if cls._instance is None:
      cls._instance = cls(country, capital, leader)
    return cls._instance

# methods for displaying info, changing the leader and getting the GDP
  def display_info(self): 
    print(f"The government of {self.country} is an excellent example of the Singleton pattern.")
    print(f"Country: {self.country}")
    print(f"Capital: {self.capital}")
    print(f"Leader: {self.leader}")
    print(f"A country can have only one official government.")
    print(f"Regardless of the personal identities of the individuals who form governments, the title, 'The Government of {self.country}', is a global point of access that identifies the group of people in charge.")


  def change_leader(self, new_leader):
        print(f"Changing leader of {self.country} government from {self.leader} to {new_leader}.")
        self.leader = new_leader
 
 
  def get_gdp(self):
        # Dummy function to calculate GDP (just for illustration)
        gdp = 1000  # Placeholder value
        return gdp



# Usage of the government class with the United States:
def main():
    # Creating instance of Government
    government = Government.get_instance("United States", "Washington D.C.", "President Biden")
 
 
    # Display information
    government.display_info()
 
 
    # Change leader
    government.change_leader("President Harris")
    print("Updated information:")
    government.display_info()
 
 
    # Get GDP
    gdp = government.get_gdp()
    print(f"GDP of {government.country}: {gdp}")
 
 
if __name__ == "__main__":
    main()
