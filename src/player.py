# Write a class to hold player information, e.g. what room they are in currently.
# instance method == only used by the object
# class variable == shared between all players - maybe a class name - all instances of that class 
# static method == same as above

class Player:
    # Init player with name 
    def __init__(self, name, starting_room):
        self.name = name
        # Player also has attr current_room - every player needs to be in a room to start playing 
        self.current_room = starting_room
    
    def travel(self, direction):
        # Player should be able to move in a direction
        print(f"Player should travel {direction}")
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You cannot move in that direction.")

    
    
