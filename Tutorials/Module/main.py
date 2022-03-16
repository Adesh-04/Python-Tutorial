# from converter import kgs_to_lbs

# try:
#     weight = int(input("Your weight in Kgs: "))
#     print(kgs_to_lbs(weight))
# except ValueError:
#     print("enter only integer")


# -------------------------------------------------------------------------------------

# from utils import find_max

# list = [1,2,5,1,3,22,1,0]

# print(find_max(list))

# --------------------------------------------------------------

# import random
# from dice import Dice


# tuple1= ( (random.randint(1,6),random.randint(1,6)),(random.randint(1,6),random.randint(1,6)) )

# object = Dice()
# object.roll(tuple1)

#---------------------------------------------------------------

from pathlib import Path


path = Path('../Python')  #you can add args as a directory or it will take current directory

# mkdir will make directory
# rmdir will remove directory
print(path.exists())   # exists will give boolean value



for file in path.glob('*.py'):
    print(file)


