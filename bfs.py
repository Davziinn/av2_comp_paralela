import time
from collections import deque

def bfs(grafo, start, end):
    fila = deque([[start]])
    caminhos = []
    while fila:
        caminho = fila.popleft()
        no = caminho[-1]
        if no == end:
            caminhos.append(caminho)
        for vizinho in grafo[no]:
            if vizinho not in caminho:
                fila.append(caminho + [vizinho])
    return caminhos

start_time = time.time()
resultados_serial = bfs(grafo, 'A', 'F') # type: ignore
end_time = time.time()

print("Execução Serial - Caminhos encontrados:")
for c in resultados_serial:
    print(c)
print(f"Tempo Serial: {end_time - start_time:.6f} segundos")