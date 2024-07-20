from random import choice
from math import log10, ceil

# OLD GRAPH CLASS
# class Graph():
#     def __init__(self,):
#         self.graph = dict()

#     def add_neighbor(self, vertex: int, neighbor: int):
#         """Adds edge from vertex to neighbor.
    
#         This function will add vertex to the graph if it is not already in it.
#         """
#         try:
#             self.graph[vertex].append(neighbor)
#         except KeyError: 
#             self.graph.update({vertex: [neighbor]})

#     def add_vertex(self, vertex: int):
#         """Adds a vertex to the graph with no neighbors."""

#         self.graph.update({vertex: []})

#     def __len__(self):
#         return len(self.graph)
    
#     def __contains__(self, item):
#         return item in self.graph.keys()
    
#     def __iter__(self):
#         return self.graph.keys()
    
#     def __repr__(self):
#         return repr(self.graph)
    
#     def __getitem__(self, key):
#         return self.graph[key]

class Graph(list):
    """Graph class implemented using an adjacency list.
    
    Graph is implemented as a list with each index acting as a vertex and its neighbors as its value.
    """
    def __init__(self, size):
        """Initialize list of size with initial values being an empty list."""
        super().__init__([[] for _ in range(size[0] * size[1])])

    def add_edge(self, vertex: int, other: int):
        """Add edge from vertex to other."""
        try:
            return self[vertex].append(other)
        except IndexError:
            return "Vertex out of bounds."


class Maze(Graph):
    def __init__(self, size):
        super().__init__(size)
        self.size = size
        self.length = size[0] * size[1]

        self.vertices = set()
        self.added = []

    def step(self) -> tuple[int]:
        """Step through maze generation.
        
        Returns newly added vertex or vertices
        or True if fully generated
        or None on fail.
        """
        # Check if fully generated.
        if len(self.added) >= self.length:
            return True
        
        # Check to see if vertices is empty.
        if len(self.vertices) == 0:
            # if so, initialize it with a random vertex
            r = choice(range(self.length))
            self.vertices.add(r)
            self.added.append(r)
            return [r]
        
        # MAIN LOOP STARTS HERE
        #
        # Here is an implementation of Prim's algorithm for maze generation. Since all edge weights are equal,
        # this implementation chooses a random adjacent vertex to add in each step.

        # Choose a random vertex and get its adjacent vertices.
        vertex = choice(list(self.vertices))
        neighbors = self.get_neighbors(vertex)

        # Remove neighbors which are already a part of the maze.
        neighbors = [n for n in neighbors if n not in self.added]

        # If there are no neighbors...
        if len(neighbors) == 0:
            # remove vertex from current list of available vertices.
            self.vertices.remove(vertex)
            return
        
        # Else, choose a random neighbor to add to the maze from vertex.
        other = choice(neighbors)
        self.add_edge(vertex, other)
        self.add_edge(other, vertex)
        self.vertices.add(other)
        self.added.append(other)
        return [vertex, other]


    def get_neighbors(self, vertex) -> list[int]:
        """Calculate and return a list of neighbors for a vertex."""

        raise NotImplementedError("Parent class \"Maze\" does not implement \"get_neighbors().\" Consider using inheriting classes such as \"SquareMaze\" or \"HexMaze\".")
    

class SquareMaze(Maze):
    """Maze made up of square tiles."""

    def get_neighbors(self, vertex) -> list[int]:
        """Calculate and return a list of neighbors for a vertex in a square maze."""

        w, h = self.size
        neighbors = []
        row, col = divmod(vertex, w)

        # If left neighbor exists.
        if col != 0:
            neighbors.append(vertex-1)

        # If top neighbor exists.
        if row != 0:
            neighbors.append(vertex-w)

        # If right neighbor exists.
        if col != w-1:
            neighbors.append(vertex+1)

        # If bottom neighbor exists.
        if row != h-1:
            neighbors.append(vertex+w)

        return neighbors
    
class TriangleMaze(Maze):
    """Maze made up of triangle tiles."""

    def get_neighbors(self, vertex) -> list[int]:
        """Calculate and return a list of neighbors for a vertex in a triangle maze."""

        w, h = self.size
        neighbors = []
        row, col = divmod(vertex, w)

        # If left neighbor exists.
        if col != 0:
            neighbors.append(vertex-1)

        # If right neighbor exists.
        if col != w-1:
            neighbors.append(vertex+1)

        # Determine if row and col are even or odd.
        row_even = row % 2 == 0
        col_even = col % 2 == 0

        # For triangles that are pointing up...
        if (row_even and col_even) or (not (row_even or col_even)):
            # if bottom neighbor exists
            if row != h-1:
                neighbors.append(vertex+w)

        # For bottom pointing triangles...
        else:
            # if top neighbor exists
            if row != 0:
                neighbors.append(vertex-w)

        return neighbors


if __name__ == "__main__":

    size = (3, 3)
    
    print(f"\nCreating graph of size: {size}")
    g = Graph(size)
    print(f"\t{g}\n")

    print("Adding edge from 1 to 2...")
    g.add_edge(1, 2)
    print(f"\t{g}\n")

    print(f"Creating square maze of size: {size}\n")
    m = SquareMaze(size)

    print("Generating maze...")
    while m.step() != None:
        pass

    print(f"\t{m}\n")

    size = (7, 4)

    print(f"Creating triangle maze of size: {size}\n")
    t = TriangleMaze(size)

    print("Generating maze...")
    while t.step() != None:
        pass

    print(f"\t{t}\n")


# OLD MAZE CLASS
# class Maze():
#     def __init__(self, size):
#         self.maze = Graph()
#         self.size = size
#         self.generate_maze(size)

#     def generate_maze(self, size):
#         """Generates the maze using a simplified version of Prim's Algorithm."""
        
#         width, height = size

#         start = choice(range(width * height))  # Get a random starting vertex in the maze.
#         vertices = [start]
#         while len(self.maze) < width * height:
            
#             # Choose a random vertex to continue the maze at.
#             _vertex = choice(vertices)

#             # Get neighbors of vertex.
#             neighbors = Maze.get_neighbors(_vertex, width, height)

#             # Ensure all neighbors are not apart of the maze yet.
#             good_neighbors = [n for n in neighbors if n not in self.maze]

#             # If there are no neighbors...
#             if len(good_neighbors) == 0:
#                 # Remove vertex from vertices and continue.
#                 vertices.remove(_vertex)
#                 continue
            
#             # Else we choose and add a new neighbor to the maze from _vertex.
#             _neighbor = choice(good_neighbors)
#             self.maze.add_neighbor(_vertex, _neighbor)
#             self.maze.add_neighbor(_neighbor, _vertex)
#             vertices.append(_neighbor)


#     @staticmethod
#     def get_neighbors(vertex: int, width: int, height: int):
#         """Calculates and returns the neighbors of a given vertex given maze width and height."""

#         neighbors = []

#         # if left neighbor exists
#         if vertex % width != 0:
#             # add left neighbor
#             neighbors.append(vertex-1)

#         # if top neighbor exists
#         if vertex // width != 0:
#             # add top neighbor
#             neighbors.append(vertex-width)

#         #if right neighbor exists.
#         if vertex % width != width-1:
#             # add right neighbor
#             neighbors.append(vertex+1)

#         # if bottom neighbor exists.
#         if vertex // width != height-1:
#             # add bottom neighbor
#             neighbors.append(vertex+width)

#         return neighbors
    
#     def __repr__(self):
#         return repr(self.maze)
    
#     def __str__(self):
#         """Returns a graphical string representation of the maze."""

#         width, height = self.size
#         maze_string = ""
#         maze_length = width * height
#         number_length = ceil(log10(maze_length-1))

#         # Iterate through the maze line by line
#         for v in range(0, maze_length, width):
#             _cur = ""
#             _next = ""

#             for i in range(width):
#                 _cur += f"{str(v+i):<{number_length}}"

#                 neighbors = self.maze.graph[v+i]
#                 _cur += " - " if v+i+1 in neighbors else "   "
#                 _next += f"{'|':<{number_length+3}}" if v+i+width in neighbors else " " * number_length + "   "
            
#             maze_string += _cur + "\n" + _next + "\n"

#         return maze_string
    
#     def __getitem__(self, key):
#         return self.maze[key]