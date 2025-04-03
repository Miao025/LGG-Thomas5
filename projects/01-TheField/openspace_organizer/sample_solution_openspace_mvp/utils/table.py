class Seat:
    #Initialize class with attributes free and occupant
    def __init__(self):
        self.free = True
        self.occupant  = ""

    def set_occupant(self, name):
        """ Allows the program to assign someone a seat if it's free"""
        if self.free:
            self.free = False
            self.occupant = name

    def remove_occupant(self):
        """Remove someone from a seat and return the name of the person occupying the seat before"""
        name = self.occupant
        self.free = True
        self.occupant = ""
        return name
    
class Table:
    def __init__(self):
        self.capacity = 4
        self.seats = [Seat() for _ in range(self.capacity)]

    def has_free_spot(self):
        """ Returns a boolean (True if a spot is available)"""
        if self.left_capacity() > 0:
            return True
        else:
            return False
                
    def assign_seat(self,name):
        """ Places someone at the table"""
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                break


               
            
    def left_capacity(self):
        """ Returns an integer of how many free spots are left at the table"""
        free_spots = 0
        for seat in self.seats:
            if seat.free:
                free_spots += 1
        return free_spots
