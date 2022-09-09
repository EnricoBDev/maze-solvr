import numpy as np
from maze import Maze
from vertex import Vertex

def check_color(img, i, j, maze_matrix):
    BLACK = (0, 0, 0, 255)
    WHITE = (255, 255, 255, 255)
    BLUE = (0, 0, 255, 255)
    if np.array_equal(img[i][j], WHITE):
        maze_matrix[i][j] = 1
    if np.array_equal(img[i][j], BLACK):
        maze_matrix[i][j] = 0      
    if np.array_equal(img[i][j], BLUE):
        maze_matrix[i][j] = 2   

def create_maze(img):
    rows = len(img)
    columns = len(img[0])
    maze_matrix = np.zeros((rows, columns), dtype = int)
    start_end = []
    for i in range(rows):
        for j in range(columns):
            for _ in range(0, 3):
                check_color(img, i, j, maze_matrix)
    for i in range(rows):
        for j in range(columns):
            if maze_matrix[i][j] == 2:
                start_end.append(Vertex((i,j)))
    if len(start_end) != 2:
        return False
    else:
        return Maze(start_end[0], start_end[1], maze_matrix)


# driver code for testing purposes
# im = Image.open(r"C:\Users\bassi\Documents\PythonScripts\maze_solver\maze.png")
# array = np.array(im)
# print(create_maze(array))