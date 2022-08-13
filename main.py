import numpy as np
import cv2

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



img = cv2.imread("maze.png")
maze = np.zeros((len(img), len(img[0])), dtype = int )

maze = create_maze(img, maze)
adj_list = create_adj_list(maze.matrix)
path = solve(maze, adj_list)

completed = draw_path(img, path, int())

cv2.imwrite("completed.png", resized)
cv2.namedWindow("Completed Maze", cv2.WINDOW_NORMAL)
cv2.imshow("Completed Maze", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()