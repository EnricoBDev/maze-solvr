class Maze:
    def __init__(self, start, end, matrix):
        self.start = start
        self.end = end
        self.matrix = matrix
        self.height = len(matrix)
        self.width = len(matrix[0])

    def __repr__(self):
        return f"Maze start: {self.start}, end: {self.end}"