# Criar resumos de artigos em PDF

Este projeto utiliza a biblioteca Langchain para resumir artigos em PDF. O código define duas funções principais: `resumir_texto` e `executar_programa`. A primeira função recebe um texto como entrada e retorna um resumo desse texto. A segunda função processa uma lista de endereços de arquivos PDF, extrai o texto de cada PDF, resumindo-o e salvando o resultado em um arquivo TXT. O projeto também define uma classe `Artigo` que representa um artigo em PDF, com atributos como endereço, título, texto e resumo.


## Como usar

Para utilizar este projeto, siga os passos abaixo:

1. Instale as dependências necessárias executando `pip install -r requirements.txt` no terminal.
2. Crie um arquivo `.env` na raiz do projeto e adicione suas chaves de acesso à API do OpenAI:
    
    OPENAI_API_KEY="sua chave de acesso à API do OpenAI"
    
    MODEL_NAME="nome do modelo desejado"
    
3. Coloque os arquivos PDF que deseja resumir na pasta `pdfs`.
4. Execute o programa com `python main.py`. Os resumos serão salvos na pasta `resumos` em arquivos TXT separados.
