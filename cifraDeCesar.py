# Armazenando o alfabeto na variável alfabeto
alfabeto = 'abcdefghijklmnopqrstuvwxyz'


def Encriptar(mensagem,chave):
    
    recebeAlfabeto = ''
    # Para cada letra na minha mensagem
    for letra in mensagem:
        
        # If para poder escrever a mensagem com espaços, sem dar erro.
        if letra in alfabeto:
            # Crio uma variável que recebe o index de cada letra no alfabeto
            letra_index = alfabeto.index(letra)
            
            
            
            # Quem eu quero, está nesse alfabeto (alfabeto) nesse index alfabeto(letra_index) mais a chave que é o número a frente (alfabeto[letra_index + chave])
            # recebeAlfabeto += alfabeto[letra_index + chave]
            # Agora eu preciso guardar isso em uma variável, criando uma variável vazia (variavel = '')
            
            #Agora para poder retornar o vetor a 0 se for mais do que as 25 opções da variavel alfabeto, eu preciso pegar o resto da divisão de 26
            # A variável recebeAlfabeto recebe o alfabeto + a chave e o resto da divisao do tamanho do alfabeto (26) que é igual a 1
            # Somamos a chave e dividimos pelo tamanho do alfabeto e pegamos o resto da divisão
            # recebeAlfabeto += alfabeto[(letra_index + chave) % 26]
            # Quando o índice for 26 % 26, o resto é 0, 27 resto 1, 28 resto 2 e assim sucessivamente, assim voltando desde o começo do alfabeto novamente             
            recebeAlfabeto += alfabeto[(letra_index + chave) % len(alfabeto)]
            
        
        else:
            recebeAlfabeto += letra
        
    return recebeAlfabeto

def Desencriptar(mensagem,chave):
    
    recebeAlfabeto = ''
    # Para cada letra na minha mensagem
    for letra in mensagem:
        
        if letra in alfabeto:
            # Crio uma variável que recebe o index de cada letra no alfabeto
            letra_index = alfabeto.index(letra)
            
            # Quem eu quero, está nesse alfabeto (alfabeto) nesse index alfabeto(letra_index) mais a chave que é o número a frente (alfabeto[letra_index + chave])
            # recebeAlfabeto += alfabeto[letra_index + chave]
            # Agora eu preciso guardar isso em uma variável, criando uma variável vazia (variavel = '')
            
            #Agora para poder retornar o vetor a 0 se for mais do que as 25 opções da variavel alfabeto, eu preciso pegar o resto da divisão de 26
            # A variável recebeAlfabeto recebe
            recebeAlfabeto += alfabeto[(letra_index - chave) % len(alfabeto)]
        
        else:
            recebeAlfabeto += letra
        
    return recebeAlfabeto
        
        

def main():
    
    mensagem = str(input("Qual a mensagem:"))
        
    chave = int(input("Qual é a chave:"))
    

    print('''[ 1 ]- Para Encriptar''')
    print('''[ 2 ]- Para Descriptar''')
    
    option = int(input("Selecione a Opção:"))
    
    if option == 1:
        
        encriptar = Encriptar(mensagem,chave)
        
        print(encriptar)
       

    elif option == 2:
        
        desencriptar = Desencriptar(mensagem,chave)
        
        print(desencriptar)
         
    else:
        print("Comando Inválido")
        
        

if __name__ == '__main__':
    main()