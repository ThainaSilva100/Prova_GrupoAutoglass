'''
Escreva um programa contendo uma função que receba uma lista de inteiros.
Exemplo de entrada da função: [1, 2, 3, 4, 5, 6, 7, 8]
- A função deve mostrar todos os números pares da lista.
- A função deve ter type hints nas variáveis de entrada.
- A função deve ter tratativa de erros caso o valor nao seja um número inteiro.
- Use if __name__ == "__main__" para executar a função.
'''

# Importando uma lista
from typing import List

# Função para encontrar os números pares da lista
def numeros_pares(lista: List[int]):
    try:
        # Verificando se todos os elementos da lista são inteiros
        for num in lista:
            if not isinstance(num, int):

                # Se der erro, informa uma mensagem de exceção
                raise ValueError("Todos os elementos da lista devem ser números inteiros.")
        
        # Exibindo os números pares da lista
        pares = [num for num in lista if num % 2 == 0]
        print("Números pares:", pares)
    
    # Se der erro, informa uma mensagem de exceção
    except ValueError as e:
        print(e)

# Executando a função se o arquivo for rodado diretamente
if __name__ == "__main__":

    # Exemplo de lista de entrada
    lista = [1, 2, 3, 4, 5, 6, 7, 8]
    
    # Chamando a função para retornar os números pares
    numeros_pares(lista)