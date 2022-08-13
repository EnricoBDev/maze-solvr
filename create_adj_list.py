from vertex import Vertex        

def traverse(row, column, direction, matrix):
    if matrix[row][column] == 2 or matrix[row][column] == 1:
        return (row, column)
    else:
        if(matrix[row][column] != 1):
            return (-1, -1)
    if direction == 0:
        if(row <= 0):
            return (-1, -1)
        else:
            return traverse(row-1, column, direction, matrix)
    if direction == 1:
        if(column >= len(matrix[1])):
            return (-1, -1)
        else:
            return traverse(row, column+1, direction, matrix)
    if direction == 2:
        if(row >= len(matrix)):
            return (-1, -1)
        else:
            return traverse(row+1, column, direction, matrix)
    if direction == 3:
        if(column <= 0):
            return (-1, -1)
        else:
            return traverse(row, column-1, direction, matrix)

def traverse_start(row, column, direction, matrix):
    if direction == 0:
        if(row <= 0):
            return (-1, -1)
        else:
            return traverse(row-1, column, direction, matrix)
    if direction == 1:
        if(column >= len(matrix[1]) or column == len(matrix[1]) - 1):
            return (-1, -1)
        else:
            return traverse(row, column+1, direction, matrix)
    if direction == 2:
        if(row >= len(matrix) or row == len(matrix) - 1):
            return (-1, -1)
        else:
            return traverse(row+1, column, direction, matrix)
    if direction == 3:
        if(column <= 0):
            return (-1, -1)
        else:
            return traverse(row, column-1, direction, matrix)

def create_adj_list(matrix):
    vert_list = []
    adj_list = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2 or matrix[i][j] == 1:
                for d in range(0, 4):
                    if(traverse_start(i, j, d, matrix) != (-1, -1)):
                        vert_list.append(Vertex(traverse_start(i, j, d, matrix)))
                if vert_list != []:
                    adj_list[Vertex((i, j)).__repr__()] = vert_list
            vert_list = []
    return adj_list