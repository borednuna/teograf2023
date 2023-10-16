# Import the networkx library for graph operations
import networkx as nx
import tkinter as tk

class Knight:
    def __init__(self) -> None:
        self.chessboard = nx.Graph()
        self.rows = 8
        self.cols = 8

        for row in range(self.rows):
            for col in range(self.cols):
                square = (row, col)
                self.chessboard.add_node(square)

        self.legal_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                        (1, -2), (1, 2), (2, -1), (2, 1)]

        for node in self.chessboard.nodes():
            for move in self.legal_moves:
                next_row, next_col = node[0] + move[0], node[1] + move[1]
                if 0 <= next_row < self.rows and 0 <= next_col < self.cols:
                    target_square = (next_row, next_col)
                    self.chessboard.add_edge(node, target_square)

    def knight_tour(self, start):
        path = [start]
        visited = [start]
        self._knight_tour(start, visited, path)
        return path
    
    def _knight_tour(self, current, visited, path):
        if len(visited) == self.rows * self.cols:
            return True
        
        for neighbor in self.chessboard.neighbors(current):
            if neighbor not in visited:
                visited.append(neighbor)
                path.append(neighbor)
                if self._knight_tour(neighbor, visited, path):
                    return True
                visited.pop()
                path.pop()
        
        return False
    
    def print_tour(self, path):
        # represent square as 1-8 (row) and a-h (column)
        for square in path:
            row = chr(square[0] + 97)
            col = square[1] + 1
            print(row + str(col), end=" ")
        print()

    def visualize_tour(self, path):
        # create a window
        window = tk.Tk()
        window.title("Knight's Tour")
        window.geometry("500x500")

        # create a canvas
        canvas = tk.Canvas(window, width=500, height=500)
        canvas.pack()

        # draw chessboard
        for row in range(self.rows):
            for col in range(self.cols):
                if (row + col) % 2 == 0:
                    color = "white"
                else:
                    color = "black"
                canvas.create_rectangle(row * 50, col * 50, (row + 1) * 50, (col + 1) * 50, fill=color)

        # draw knight's path
        for i in range(len(path) - 1):
            canvas.create_line(path[i][0] * 50 + 25, path[i][1] * 50 + 25, path[i + 1][0] * 50 + 25, path[i + 1][1] * 50 + 25, width=3, fill="red")

        # run the window's main loop
        window.mainloop()

knight = Knight()
path = knight.knight_tour((0, 0))
knight.print_tour(path)
knight.visualize_tour(path)
