# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
#
# number of cans = (wall height x wall width) ÷ coverage per can.
#
# e.g. Height = 2, Width = 4, Coverage = 5
#
# number of cans = (2 * 4) / 5
import math


def _paint_area_calculator(height,width,cover):
    no_of_cans = math.ceil((height * width) / cover)

    return no_of_cans

print(f"You'll need $ {_paint_area_calculator(2,4,5)} cans of paint.")

