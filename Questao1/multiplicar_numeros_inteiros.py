'''
Escreva um programa contendo uma função que tenha como parâmetros de entrada dois números inteiros.
- A função deve executar a multiplicação dos dois números.
- A função deve ter type hints nas variáveis de entrada e no retorno.
- A função deve converter os números em inteiros caso não sejam.
- A função deve ter tratativa de erros caso os parâmetros não sejam números.
- A função deve retornar o resultado.
- Use if __name__ == "__main__" para executar a função.     
'''

# Função para converter valores para inteiro usando type hints
def converter_para_inteiro(valor: str) -> int:
    try:
        # Verificando se o valor é float (decimal) para converter em inteiro
        numero = float(valor)
        return int(numero)  # Convertendo para inteiro após verificação
    
    except ValueError:
        # Se der erro, informa uma mensagem de exceção
        raise ValueError(f"O valor '{valor}' não pode ser convertido para um número inteiro.")

# Função para multiplicar os números inteiros usando type hints
def multiplicar_numeros(num1: str, num2: str) -> int:

    # Garantindo que os dois números sejam inteiros usando a função de conversão como validação
    num1 = converter_para_inteiro(num1)
    num2 = converter_para_inteiro(num2)
    
    # Realiza a multiplicação
    return num1 * num2

# Executando a função se o arquivo for rodado diretamente
if __name__ == "__main__":
    try:
        # Inserindo os números que devem ser multiplicados
        num1: str = input("Digite o primeiro número: ")
        num2: str = input("Digite o segundo número: ")

        # Chamando a função de multiplicação e exibindo o resultado
        resultado: int = multiplicar_numeros(num1, num2)
        print(f"O resultado da multiplicação é: {resultado}")

    # Se der erro, informa uma mensagem de exceção
    except ValueError as e:
        print(e)