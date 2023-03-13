alfabeto = 'abcdefghijklmnopqrstuvwxyz'

alfabeto_cifrado = 'qwertyuiopasdfghjklzxcvbnm'



def Encriptar(mensagem):
    
    recebeAlfabeto = ''
   
    for letra in mensagem:
        
       
        if letra in alfabeto:
           
            letra_index = alfabeto.index(letra)
              
            recebeAlfabeto += alfabeto_cifrado[letra_index]
            
        
        else:
            recebeAlfabeto += letra
        
    return recebeAlfabeto

def Desencriptar(mensagem):
    
    recebeAlfabeto = ''
    
    for letra in mensagem:
        
        if letra in alfabeto_cifrado:
           
            letra_index = alfabeto_cifrado.index(letra)
            
          
            recebeAlfabeto += alfabeto[letra_index]
        
        else:
            recebeAlfabeto += letra
        
    return recebeAlfabeto
        
        

def main():
    
    mensagem = str(input("Qual a mensagem:"))
        
    print('''[ 1 ]- Para Encriptar''')
    print('''[ 2 ]- Para Descriptar''')
    
    option = int(input("Selecione a Opção:"))
    
    if option == 1:
        
        encriptar = Encriptar(mensagem)
        
        print(encriptar)
       

    elif option == 2:
        
        desencriptar = Desencriptar(mensagem)
        
        print(desencriptar)
         
    else:
        print("Comando Inválido")
        
        

if __name__ == '__main__':
    main()