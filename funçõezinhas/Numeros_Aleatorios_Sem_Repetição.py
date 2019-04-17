from random import randint
#Função pra gerar número com um parametro de quantidade e o intervalo
def gerar(quantidade,mini,maxi):
    numerosSorteados = []
    #cria uma lista local para ser retornada ao fim da execução e ser reiniciada
    #caso seja preciso a função seja chamada novamente.
    if (quantidade > abs(mini-maxi)): #Verifica se a quantidade é maior do queo intervalo
        quantidade = abs(mini-maxi)
        #Atribui o Intervalo a variavel quantidade
        #para gerar o maximo de numeros possiveis
        print("#Quantidade de números a serem gerados é maior que o intervalo solicitado, gerando só os possíveis#: ")
    while(len(numerosSorteados) <= quantidade):
        #usa a quantidade como parametro para parada
        numero=randint(mini,maxi)
        #Gera um número entre o intervalo solicitado
        if numero in numerosSorteados:
          #Se o número sorteado já estiver na lista
          continue #Ele volta e gera outro número
        else:
          numerosSorteados.append(numero)
          #Adiciona o número na lista para entrar na proxima verificação
    return numerosSorteados #retorna a lista para onde a função foi chamada


"""Exemplos"""
num = gerar(10,0,5)
'''Passar os parâmetros para gerar, caso
a quantidade de números solicitados for maior do que o intervalo a função limita a
quantidade de números a serem gerados automaticamente'''
print(num)
print("="*80)
num2 = gerar(7,10,50)
print(num2)
