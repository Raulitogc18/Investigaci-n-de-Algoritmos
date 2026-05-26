from astar import astar


def print_grid(grid, path=None):
    """
    Imprime la cuadrícula y el camino.
    """

    for i in range(len(grid)):
        row = ""

        for j in range(len(grid[0])):

            if path and (i, j) in path:
                row += " * "
            elif grid[i][j] == 1:
                row += " # "
            else:
                row += " . "

        print(row)

    print()


grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

path = astar(grid, start, end)

if path:
    print("Camino encontrado:")
    print(path)
    print_grid(grid, path)
else:
    print("No existe un camino.")