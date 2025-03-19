'''
Analise a estrutura de diretórios abaixo e explique sobre cada pasta/arquivo 
apresentado, e implemente um código simples com os seguintes passos:

- A partir do main.py realizar a chamada de uma função ‘ola_mundo()’ presente 
no arquivo src/ola_mundo.py que deve retornar uma string com uma mensagem 
qualquer.
- Utilizar o if __name__ == "__main__" para executar a função.
- Demonstrar como importar a função de outro arquivo.

Estrutura de diretórios:
| .venv         
| assets        
| src/          
 __init__.py    
 ola_mundo.py   
| logs/         
 logs.log       
| main.py       
| .gitignore    
| requirements.txt  
| README.md     
'''

''''

## Explicação do diretório:

| .venv 
--> Pasta onde fica o ambiente virtual do Python, contém todas as dependências do projeto, pacotes e bibliotecas 
garantindo que não haja conflitos de diferentes versões entre eles.

| assets      
--> Pasta que contém vários tipos de arquivos utilizados no projeto, como imagens, CSS e JavaScript ou demais tipos
de recursos que um projeto possa usar, facilitando sua organização.

| src/   
--> Pasta onde fica os arquivos principais (código-fonte) do projeto, armazena pastas e arquivos que constroem
toda a lógica do projeto.

 __init__.py    
 --> Este arquivo funciona como um inicializador de pacotes, fazendo com que um diretório se torne um pacote e o
 Python consiga importar seus arquivos.

 ola_mundo.py 
 --> Arquivo Python que contém a função "ola_mundo" e será chamado no arquivo main. 

| logs/    
--> Pasta onde fica armazenado oa logs do projeto.

 logs.log 
 --> Arquivo onde fica armazenado logs (registros de eventos ou erros) gerados durante toda a execução do projeto.

| main.py 
--> Arquivo principal de execução do projeto, no qual será chamada a função "ola_mundo()" do arquivo "ola_mundo".  

| .gitignore    
--> Este arquivo serve para não versionar (ignorar) pastas ou outros arquivos que não devem ser importados 
no Git, como o ambiente virtual (.venv) ou arquivos temporários.

| requirements.txt  
--> Este arquivo lista todas as dependências do projeto (bibliotecas) que fazem o projeto funcionar.

| README.md 
--> Este arquivo serve como um documento sobre o projeto, contendo informações sobre o mesmo, e demais informações
como instalações necessárias para funcionamento, configurações, tecnologias usadas, como fazer o projeto funcionar
e demais informações que o desenvolvedor acredita ser importante de ser mencionada.

'''