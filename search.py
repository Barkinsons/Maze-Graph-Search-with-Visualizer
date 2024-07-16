# from math import abs


class a_star:
    """Graph search glass for a star graph search."""

    class Cell:
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
        


    def __init__(self, graph, start, dest, app):
        self.open = [a_star.Cell(start, start, 0, 0, 0)]
        self.closed = []
        self.graph = graph
        self.dest = dest
        self.app = app

    def step(self):
        if len(self.open) > 0:
            q = self.open.pop()

            for s in self.graph[q.vertex]:
                if s == self.dest:
                    self.app.change_tile(s, (255, 0, 0))
                    return True
            
                cell = a_star.Cell(s, q)
                cell.g = 1
                cell.h = self.calculate_h(s, self.dest)
                cell.f = cell.g + cell.h

                if cell in self.open or cell in self.closed:
                    continue
                
                self.open.append(cell)
                # print(self.open)

            self.closed.append(q)
            print(self.closed)
            self.app.change_tile(q.vertex, (0, 0, 255))
            self.open.sort(key=lambda x: x.f, reverse=True)

    def calculate_h(self, src, dest):
        sx, sy = divmod(src, self.graph.size[0])
        dx, dy = divmod(dest, self.graph.size[0])

        return abs(sx - dx) + abs(sy - dy)
    