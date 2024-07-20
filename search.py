from settings import Settings


class a_star:
    """Graph search glass for a*."""


    class Cell:
        """Cell class for holding a* search values."""

        def __init__(self, vertex, parent=None, f=float("inf"), g=float("inf"), h=0):
            self.vertex = vertex
            self.parent = parent
            self.f = f
            self.g = g
            self.h = h

        def __repr__(self):
            return str(self.vertex)
        
        def __eq__(self, other):
            return other.vertex == self.vertex


    def __init__(self, graph, start, dest):
        self.open = [a_star.Cell(start, None, 0, 0, 0)]
        self.closed = []
        self.graph = graph
        self.dest = dest
        self.solution = None


    def step(self):
        """Step through a* graph search."""

        # Ensure a non-empty list before starting.
        if len(self.open) > 0:

            # Pop the next "best" vertex.
            q = self.open.pop()

            # Get neighbors of q.
            for s in self.graph[q.vertex]:

                # If neighbor is our destination we found it!
                if s == self.dest:
                    return (True, [q.vertex, s])
            
                # Else create a new cell and calculate its values.
                cell = a_star.Cell(s, q)
                cell.g = 1
                cell.h = self.calculate_h(s, self.dest)
                cell.f = cell.g + cell.h

                # If cell is already in open or closed ignore it.
                if cell in self.open or cell in self.closed:
                    continue
                
                # Else add it to the open list.
                self.open.append(cell)

            # Add q to the closed list.
            self.closed.append(q)

            # Sort open list.
            self.open.sort(key=lambda x: x.f, reverse=True)

            return (False, [q.vertex])
        
    def sol_step(self):

        if not self.solution:
            pass

    def calculate_h(self, src, dest):
        """h function for a* search (manhattan distance)."""

        sx, sy = divmod(src, self.graph.size[0])
        dx, dy = divmod(dest, self.graph.size[0])

        return abs(sx - dx) + abs(sy - dy)
    