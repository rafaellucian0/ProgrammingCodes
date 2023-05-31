numeros = [];
soma = 0;
quantidade = int(input());
for i in range(0, quantidade):
    num_atual=int(input());
    if(num_atual)!=0:
        numeros.append(num_atual);
    else:
        numeros.remove(numeros[len(numeros)-1]);
for i in numeros:
    soma+=i;
print(soma);