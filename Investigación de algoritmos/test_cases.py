from astar import astar


def run_tests():

    # Caso 1: Camino simple
    grid1 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    print("Caso 1")
    print(astar(grid1, (0, 0), (2, 2)))
    print()

    # Caso 2: Obstáculos
    grid2 = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    print("Caso 2")
    print(astar(grid2, (0, 0), (2, 2)))
    print()

    # Caso 3: Sin solución
    grid3 = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]

    print("Caso 3")
    print(astar(grid3, (0, 0), (2, 2)))
    print()

    # Caso borde: inicio = destino
    print("Caso borde")
    print(astar(grid1, (1, 1), (1, 1)))


run_tests()