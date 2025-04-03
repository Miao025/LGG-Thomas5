import csv
import random
from utils.table import Table

class OpenSpace:
    def __init__(self):
        self.number_of_tables = 6
        self.tables = [Table()  for _ in range(self.number_of_tables)]
                       
    def organize(self, names):
        """ Randomly assigns people to `Seat` objects in the different `Table` objects."""
        for table in self.tables:
                while table.has_free_spot():
                        name = random.choice(names)
                        table.assign_seat(name)
                        names.remove(name)
    def display(self):
        """ Display the different tables and there occupants in a nice and readable way"""
        count = 1 
        for table in self.tables:
                print("Table " + str(count) + ":")
                for seat in table.seats:
                    print(f'{seat.occupant}')
                count = count + 1

    def store(self, output_filename): 
        """ Store the repartition in an excel file"""
        with open(output_filename, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            table_no = 1
            for table in self.tables:
                seated_names = ["Table "+str(table_no)]
                for seat in table.seats:
                    seated_names.append(seat.occupant) 
                writer.writerow(seated_names)
                table_no += 1
            
        
        
        