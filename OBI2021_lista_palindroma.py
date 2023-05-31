quantidade = int(input());
entrada = input();
lista_palindroma = [];
contracoes = 0;

i=0;
tamanho = len(entrada);
while i<tamanho:
    if(entrada[i]==' ' or i==tamanho-1):
        lista_palindroma.append(int(entrada[0:i+1]));
        entrada = entrada[i+1:];
        i=0;
        tamanho = len(entrada);
    else:
        i+=1;

for i in range(0,int(quantidade/2)):
    if lista_palindroma[i]!=lista_palindroma[quantidade-i-1]:
        contracoes += 1;
print(contracoes);