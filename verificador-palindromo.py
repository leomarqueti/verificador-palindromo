import string
import re

#Função para limpar o texto
def limpa_texto(texto):

    #Deixa o texto em minuscula
    texto = texto.lower()
    
    #Tira espaço e pontuaçao do texto
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto)
    
    #Retorna o texto limpo sem maiuscula, espaços e pontuaçoes
    return texto_limpo

#Função que verifica o palindromo
def verificador_palindromo(palavra):

    #Logica para verificar o palidromo 
    if palavra == palavra[::-1]:
        return f"A palavra: {palavra} ,é um Palindromo"
    else:
        return f"A palavra: {palavra} ,NAO É um Palindromo"


def executa_sistema():

    try:

        palavra = input("Insira uma palavra: ")
        if not palavra:
            print("Insira uma palavra valida!")
            return
        
        print(verificador_palindromo(limpa_texto(palavra)))

    except ValueError:

        print("Por favor, insira um texto válido.")


executa_sistema()


input("Pressione Enter para sair...")


