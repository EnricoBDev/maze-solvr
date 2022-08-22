import numpy as np

from color_matrix import create_maze
from create_adj_list import create_adj_list
from solve import solve
from img_manipulation import draw_path

# things to implement in the ui
# buttons:
# - select image from folder
# - generate maze with dedalus
# - solve button
# - checkbox for animated gif
# show generated image and ask to regenerate it if the user wants 
# once the maze is solved ask to save it along with the optional animated gif and show it