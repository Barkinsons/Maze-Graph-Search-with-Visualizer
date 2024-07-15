from random import choice
from math import log10, ceil


class Graph():
    def __init__(self):
        self.graph = dict()

    def add_neighbor(self, vertex: int, neighbor: int):
        """Adds edge from vertex to neighbor.
    
        This function will add vertex to the graph if it is not already in it.
        """
        try:
            self.graph[vertex].append(neighbor)
        except KeyError: 
            self.graph.update({vertex: [neighbor]})

    def add_vertex(self, vertex: int):
        """Adds a vertex to the graph with no neighbors."""

        self.graph.update({vertex: []})

    def __len__(self):
        return len(self.graph)
    
    def __contains__(self, item):
        return item in self.graph.keys()
    
    def __iter__(self):
        return self.graph.keys()
    
    def __repr__(self):
        return repr(self.graph)
    
    def __getitem__(self, key):
        return self.graph[key]


class Maze():
    def __init__(self, size):
        self.maze = Graph()
        self.size = size
        self.generate_maze(size)

    def generate_maze(self, size):
        """Generates the maze using a simplified version of Prim's Algorithm."""
        
        width, height = size

        start = choice(range(width * height))  # Get a random starting vertex in the maze.
        vertices = [start]
        while len(self.maze) < width * height:
            
            # Choose a random vertex to continue the maze at.
            _vertex = choice(vertices)

            # Get neighbors of vertex.
            neighbors = Maze.get_neighbors(_vertex, width, height)

            # Ensure all neighbors are not apart of the maze yet.
            good_neighbors = [n for n in neighbors if n not in self.maze]

            # If there are no neighbors...
            if len(good_neighbors) == 0:
                # Remove vertex from vertices and continue.
                vertices.remove(_vertex)
                continue
            
            # Else we choose and add a new neighbor to the maze from _vertex.
            _neighbor = choice(good_neighbors)
            self.maze.add_neighbor(_vertex, _neighbor)
            self.maze.add_neighbor(_neighbor, _vertex)
            vertices.append(_neighbor)


    @staticmethod
    def get_neighbors(vertex: int, width: int, height: int):
        """Calculates and returns the neighbors of a given vertex given maze width and height."""

        neighbors = []

        # if left neighbor exists
        if vertex % width != 0:
            # add left neighbor
            neighbors.append(vertex-1)

        # if top neighbor exists
        if vertex // width != 0:
            # add top neighbor
            neighbors.append(vertex-width)

        #if right neighbor exists.
        if vertex % width != width-1:
            # add right neighbor
            neighbors.append(vertex+1)

        # if bottom neighbor exists.
        if vertex // width != height-1:
            # add bottom neighbor
            neighbors.append(vertex+width)

        return neighbors
    
    def __repr__(self):
        return repr(self.maze)
    
    def __str__(self):
        """Returns a graphical string representation of the maze."""

        width, height = self.size
        maze_string = ""
        maze_length = width * height
        number_length = ceil(log10(maze_length-1))

        # Iterate through the maze line by line
        for v in range(0, maze_length, width):
            _cur = ""
            _next = ""

            for i in range(width):
                _cur += f"{str(v+i):<{number_length}}"

                neighbors = self.maze.graph[v+i]
                _cur += " - " if v+i+1 in neighbors else "   "
                _next += f"{'|':<{number_length+3}}" if v+i+width in neighbors else " " * number_length + "   "
            
            maze_string += _cur + "\n" + _next + "\n"

        return maze_string
    
    def __getitem__(self, key):
        return self.maze[key]


if __name__ == "__main__":

    print("\nBuilding a 6x6 maze...\n")
    m = Maze((6, 6))

    print(m, end="")
