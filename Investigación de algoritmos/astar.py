import heapq


class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent

        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f


def heuristic(a, b):
    """
    Distancia Manhattan.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def reconstruct_path(current):
    """
    Reconstruye el camino encontrado.
    """
    path = []

    while current:
        path.append(current.position)
        current = current.parent

    return path[::-1]


def astar(grid, start, end):
    """
    Implementación del algoritmo A*.
    """

    rows = len(grid)
    cols = len(grid[0])

    # Validar posiciones
    if start == end:
        return [start]

    if grid[start[0]][start[1]] == 1:
        return None

    if grid[end[0]][end[1]] == 1:
        return None

    open_list = []
    closed_set = set()

    start_node = Node(start)
    goal_node = Node(end)

    heapq.heappush(open_list, start_node)

    while open_list:

        current_node = heapq.heappop(open_list)

        if current_node.position == goal_node.position:
            return reconstruct_path(current_node)

        closed_set.add(current_node.position)

        x, y = current_node.position

        neighbors = [
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1)
        ]

        for next_pos in neighbors:

            nx, ny = next_pos

            # Verificar límites
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                continue

            # Verificar obstáculos
            if grid[nx][ny] == 1:
                continue

            if next_pos in closed_set:
                continue

            neighbor = Node(next_pos, current_node)

            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(next_pos, end)
            neighbor.f = neighbor.g + neighbor.h

            heapq.heappush(open_list, neighbor)

    return None