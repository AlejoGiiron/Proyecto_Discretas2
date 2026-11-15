# Proyecto Matemáticas Discretas II

# Alejandro Giron - 1924418

Se estará usando uv para el manejo del ambiente.

## Punto 1
- Repositorio creado: https://github.com/AlejoGiiron/Proyecto_Discretas2

## Punto 2
- Se realiza el commit inicial: "Iniciando"

## Punto 3
Escogí la **lista de adyacencia** para representar el grafo, debido a que fue la que entendí con mayor facilidad.
- Cada nodo guarda la lista de sus nodos adyacentes junto con el peso de la arista.
- Es más fácil de programar en Python: se usa un diccionario dentro de otro.

## Punto 4
Para el grafo dirigido usé la misma representación, la **lista de adyacencia**. Solo cambia en cómo se guarda cada arista:

- En el **dirigido** importa el orden, por eso solo se anota en la lista de `source`.
- Si el nodo `target` todavía no tiene lista, le creo una **vacía**, para que el nodo exista en el grafo aunque no salgan aristas de él.

## Punto 5
Hice la función **read_graph** en **graphs.py**. Recibe la ruta de un archivo CSV y devuelve el grafo ya construido usando el separador ",".

### Test
En **data/** tenemos los ejemplos de csv y solo es correr el proyecto:
    - uv run proyecto-discretas2