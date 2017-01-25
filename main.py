from saveFile import *
from crew import CrewMember
from pprintpp import pprint as pp
        
# Read in saved game
save = SaveFile("Input/continue.sav")

# Modify?
save.mainShip.cash = 100

# Write out new file
save.write("Output/continue.sav")

