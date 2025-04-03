from utils.openspace import OpenSpace
from utils.file_utils import read_names_from_csv 


if __name__ == "__main__":
   input_filename = "new_colleagues.csv"
   output_filename = "output.csv"

   # creates a list that contains all the colleagues names
   names = read_names_from_csv(input_filename)
   
   # create an OpenSpace()
   open_space = OpenSpace()

   # assign a colleague randomly to a table
   open_space.organize(names)

   # save the seat assigments to a new file
   open_space.store(output_filename)

   # display assignments in the terminal
   open_space.display()