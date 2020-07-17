# method: a function associated with a class
# class: blue print to create each item/instances vs. instance of a class 
# instance of a class: instance variables. Contain data unique to each instance. 
# initialize class attributes
# __init__ initialize or constructor function
# self == instance as the first argument
# name & description == arguments

# class variables: variables that are shared among all instances of a class. 
# instance variables can be unique for each instance (name & description)
# class variables should be the same for each instance. 

# class Item: 
#     def __init__(self, name, description):
#         self.name = name  # instance variable
#         self.description = description
        
#     def on_take(self):
#         """ 
#         Used to perform business logic when the item is picked up by the player
#         """
#         print("\n*************************************************")
#         print(f"\nYou have picked up {self.name}.")
        
#     def on_drop(self):
#         """
#         Used to perform business logic when the item is dropped up by the player
#         """
#         print("\n*************************************************")
#         print(f"\nYou have dropped the {self.name}.")
        
#     def __getattr__(self, name):
#         """
#         Defaults to None for any attribute not in the calss currently supported
#         """
#         return None
    
#     def __str__(self):
#         """ 
#         Replacement string method for the Item class
#         """
#         return f"{self.name} - {self.description}"
    
#     def __repr__(self):
#         """
#         REPR method for the Item class
#         """
#         return f"Item({repr(self.name)}, {repr(self.description)})"
    
# class Lamp(Item):
#     def __init__(self, name, description, color):
#         super().__init__(name, description)
#         self.color = color
        
#     def __str__(self):
#         """
#         Replacement string method for the Lamp class
#         """
#         return f"{self.name} - {self.color}, {self.description}"
    
#     def __repr__(self):
#         """
#         REPR method for the Lamp class
#         """
#         return f"Lamp({repr(self.name)}, {repr(self.description)}, {repr(self.color)})"
    
# class Treasure(Item):
#     def __init__(self, name, description, value):
#         super().__init__(name, description)
#         self.value = value_error
        
#     def __str__(self): 
#         """
#         Replacement string method for the Treasure class
#         """
#         return f"{self.name} - {self.value}, {self.description}"
    
#     def __repr__(self):
#         """
#         REPR method for the Treasure class
#         """
#         return f"Treasure({repr(self.name)}, {repr(self.description)}, {repr(self.value)})"
    
#     def __repr__(self):
#         """
#         REPR method for the Diamond class
#         """
#         return f"Diamond({repr(self.name)}, {repr(self.description)}, {repr(self.value)}, {repr(self.color)})"
