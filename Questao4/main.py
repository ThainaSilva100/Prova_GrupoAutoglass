# Importando a função ola_mundo do módulo src.ola_mundo
from src.ola_mundo import ola_mundo  

# Executando a função se o arquivo for rodado diretamente
if __name__ == "__main__":  

    # Chama a função ola_mundo()
    mensagem = ola_mundo()  

    # Exibe a mensagem retornada pela função
    print(mensagem)  
