import time
from collections import deque
import concurrent.futures

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

def buscar_caminhos_parcial(args):

    grafo, no_inicial_parcial, no_final, caminho_prefixo = args
    
    caminhos_parciais = bfs(grafo, no_inicial_parcial, no_final)
    
    caminhos_completos = []
    for caminho in caminhos_parciais:
        if caminho_prefixo[0] not in caminho:
            caminhos_completos.append(caminho_prefixo + caminho)
            
    return caminhos_completos


if __name__ == "__main__":
    
    no_inicial = 'Presidência'
    no_final = 'Equipe de Backend'

    print("--- Execução Paralela ---")
    print(f"Buscando todos os caminhos de '{no_inicial}' para '{no_final}'...\n")

    inicio_paralelo = time.time()
    
    todos_os_caminhos = []
    
    vizinhos_do_inicio = grafo_empresa.get(no_inicial, [])
    
    tarefas = [(grafo_empresa, vizinho, no_final, [no_inicial]) for vizinho in vizinhos_do_inicio]
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        resultados = executor.map(buscar_caminhos_parcial, tarefas)
        
        for lista_de_caminhos in resultados:
            todos_os_caminhos.extend(lista_de_caminhos)

    fim_paralelo = time.time()
    tempo_total_paralelo = fim_paralelo - inicio_paralelo

    print("Caminhos encontrados:")
    if todos_os_caminhos:
        for c in sorted(todos_os_caminhos):
            print(f" -> {' -> '.join(c)}")
    else:
        print("Nenhum caminho encontrado.")
        
    print(f"\nTotal de caminhos: {len(todos_os_caminhos)}")
    print(f"Tempo de execução paralela: {tempo_total_paralelo:.6f} segundos")