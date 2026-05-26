# A* Pathfinding Algorithm

## Descripción

Este proyecto implementa el algoritmo A* (A Star) para encontrar el camino más corto en una cuadrícula con obstáculos.

---

## Requisitos

- Python 3.x

---

## Archivos

- `astar.py` → implementación principal del algoritmo
- `main.py` → ejemplo visual de ejecución
- `test_cases.py` → casos de prueba

---

## Cómo ejecutar

### Ejecutar ejemplo principal

```bash
python main.py
```

### Ejecutar pruebas

```bash
python test_cases.py
```

---

## Representación de la cuadrícula

- `0` = espacio libre
- `1` = obstáculo

---

## Casos de prueba incluidos

1. Camino simple
2. Camino con obstáculos
3. Camino imposible
4. Caso borde (inicio = destino)

---

## Algoritmo utilizado

El algoritmo A* utiliza:

f(n) = g(n) + h(n)

Donde:

- g(n): costo recorrido
- h(n): heurística Manhattan
- f(n): costo estimado total

---

## Autor

Proyecto académico sobre algoritmos y estructuras de datos.
