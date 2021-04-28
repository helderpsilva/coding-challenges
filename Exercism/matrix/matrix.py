class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(item) for item in row.split()] for row in matrix_string.splitlines()]
        
    def row(self, index):
        index = index - 1
        return self.matrix[index]

    def column(self, index):
        index = index - 1
        return [row[index] for row in self.matrix]