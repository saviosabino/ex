# Enter your code here. Read input from STDIN. Print output to STDOUT
def impar2sum10(inicio, fim):
    cont = 0
    for n in range(inicio, fim + 1):
        if n % 2 != 0 and str(n).count('2') :
            if sum([int(i) for i in str(n)]) > 10:
                cont += 1 ;print n
    return cont

print impar2sum10(input(), input())

'''
Crio uma função com 2 parâmetros
Crio um contador
inicio um laço usando a função range com parâmetro inicio e fim + 1, dessa
        forma a função se comporta a retornar uma lista que contem todos os
        números do intervalo, inclusive os extremos.
É escrito uma condição que verifica se o número da iteração atual é ímpar e 
        possui o algarismo 2. 
        Para verificar se o número é impar, é testado se o resto da divisão 
        por 2 é diferente de 0.
        Para verificar se possui o algarismo 2, o número é 
        convertido para texto e usado uma função membro que verifica quantas
        ocorrências existem do algarismo 2 (também convertido para texto).
        Se houver mais de uma ocorrência, a condição é verdadeira.
É escrito uma outra condição que verifica se a soma dos algarismos é maior
        que 10.
        Para isso, foi preciso converter o número para texto e depois iterar
        nesse texto de forma a retornar uma lista de caracteres, nessa mesma
        iteração cada caracter é novamente convertido para número, tendo assim,
        uma lista de números inteiros. Depois, usa-se a função sum capaz de
        somar items de uma lista e com o retorna dessa função se compara se é
        maior que 10.
Se a comparação for verdadeira o contador é incrementado.
A função criada termina retornado o valor do contador.
Por fim é impresso o valor na tela, valor que será o retorno da função criada
em que seus parâmetros são os 2 inputs que o sistema hackerrank irá fornecer.
'''

