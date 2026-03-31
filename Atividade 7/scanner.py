import re

def tokenize(texto):
    """
    Função responsável por realizar a análise léxica (tokenização) de um texto.

    Parâmetros:
        texto (str): String contendo o conteúdo do arquivo de entrada.

    Retorno:
        list: Lista de tokens (strings) identificados no texto.

    Descrição:
        A função utiliza expressões regulares para identificar três tipos de tokens:
        - Palavras (incluindo caracteres acentuados da língua portuguesa)
        - Números inteiros
        - Pontuações básicas (.,!?;:)
    """

    # Expressão regular utilizada:
    # [A-Za-zÀ-ÖØ-öø-ÿ]+  → captura palavras com ou sem acento
    # \d+                 → captura números inteiros
    # [.,!?;:]            → captura sinais de pontuação
    regex = r'[A-Za-zÀ-ÖØ-öø-ÿ]+|\d+|[.,!?;:]'

    # re.findall retorna todas as ocorrências que casam com a regex
    tokens = re.findall(regex, texto)

    return tokens


def main():
    """
    Função principal do programa.

    Responsável por:
        1. Ler o arquivo de entrada (livro.txt)
        2. Executar o processo de tokenização
        3. Exibir os tokens no terminal
        4. Salvar os tokens em um arquivo de saída

    Observação:
        O arquivo deve estar codificado em UTF-8 para suportar caracteres acentuados.
    """

    # Nome do arquivo de entrada
    arquivo = "livro.txt"

    # Abertura do arquivo em modo leitura com codificação UTF-8
    with open(arquivo, "r", encoding="utf-8") as f:
        texto = f.read()

    # Chamada da função de tokenização
    tokens = tokenize(texto)

    # Exibe os tokens no terminal
    print(tokens)

    # Salva os tokens em um arquivo de saída
    with open("saida_tokens.txt", "w", encoding="utf-8") as f:
        f.write(str(tokens))


# Ponto de entrada do programa
if __name__ == "__main__":
    main()