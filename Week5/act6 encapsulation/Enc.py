class Animal:
    def __init__(self, name, species, id=0):
        self.__name = name       # private attribute
        self.__species = species # private attribute
        self.__id = id           # private attribute

    # Getter for name
    def get_name(self):
        return self.__name
    
    # Setter for name
    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            print("Invalid name. It must be a non-empty string.")
    
    # Getter for species
    def get_species(self):
        return self.__species
    
    # Setter for species
    def set_species(self, species):
        if isinstance(species, str) and len(species) > 0:
            self.__species = species
        else:
            print("Invalid species. It must be a non-empty string.")
    

    # Getter for ID
    def get_id(self):
        return self.__id

    def set_id(self, id):
        if isinstance(id, int) and id > 0:
            self.__id = id
        else:
            print("Invalid ID. It must be a positive integer.")

    def display_info(self):
        print(f"Animal Name: {self.__name}, Species: {self.__species}, ID: {self.__id}")

class Toy:
    def __init__ (self, toy_name,toy_price):
        self._toy_name =toy_name
        self.__toy_price = toy_price

    def get_toy_name(self):
        return self._toy_name

    def get_toy_price(self):
        return self.__toy_price
    
    

# Example usage
if __name__ == "__main__":
    # Creating an animal
    lion = Animal("Leo", "Lion")
    
    # Display info using encapsulated attributes
    lion.display_info()
    
    # Access through getter
    print("Current Name:", lion.get_name())
    
    # Update using setter
    lion.set_name("Simba")
    lion.set_species("African Lion")
    lion.set_id(101)
    
    # Display updated info
    lion.display_info()
    
    # Trying invalid update
    lion.set_name("")   # This should print an error

    lion.toy = Toy("Ball", 10)
    print(f"Toy Name: {lion.toy.get_toy_name()}, Toy Price: {lion.toy.get_toy_price()}")

