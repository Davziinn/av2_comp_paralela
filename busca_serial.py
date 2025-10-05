
import time
from collections import deque

grafo_empresa = {
    'Presidência': ['Diretoria TI', 'Diretoria RH', 'Diretoria Financeira'],
    'Diretoria TI': ['Presidência', 'Gerência de Infra', 'Gerência de Dev'],
    'Diretoria RH': ['Presidência', 'Gerência de Recrutamento'],
    'Diretoria Financeira': ['Presidência', 'Gerência de Contas'],
    'Gerência de Infra': ['Diretoria TI', 'Equipe de Redes', 'Equipe de Suporte'],
    'Gerência de Dev': ['Diretoria TI', 'Equipe de Frontend', 'Equipe de Backend'],
    'Gerência de Recrutamento': ['Diretoria RH'],
    'Gerência de Contas': ['Diretoria Financeira'],
    'Equipe de Redes': ['Gerência de Infra', 'Equipe de Backend'],
    'Equipe de Suporte': ['Gerência de Infra'],
    'Equipe de Frontend': ['Gerência de Dev'],
    'Equipe de Backend': ['Gerência de Dev', 'Equipe de Redes']
}

def bfs(grafo, start, end):

    fila = deque([[start]])
    caminhos_encontrados = []
    
    if start == end:
        return [[start]]
        
    while fila:
        caminho = fila.popleft()
        no = caminho[-1]
        
        if no == end:
            caminhos_encontrados.append(caminho)
        
        for vizinho in grafo.get(no, []):
            if vizinho not in caminho:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)
                
    return caminhos_encontrados

if __name__ == "__main__":
    
    no_inicial = 'Presidência'
    no_final = 'Equipe de Backend'

    print("--- Execução Serial ---")
    print(f"Buscando todos os caminhos de '{no_inicial}' para '{no_final}'...\n")

    inicio_serial = time.time()
    
    resultados_serial = bfs(grafo_empresa, no_inicial, no_final)
    
    fim_serial = time.time()
    tempo_total_serial = fim_serial - inicio_serial

    print("Caminhos encontrados:")
    if resultados_serial:
        for c in sorted(resultados_serial):
            print(f" -> {' -> '.join(c)}")
    else:
        print("Nenhum caminho encontrado.")

    print(f"\nTotal de caminhos: {len(resultados_serial)}")
    print(f"Tempo de execução serial: {tempo_total_serial:.6f} segundos")