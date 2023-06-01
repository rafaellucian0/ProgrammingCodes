soma = int(input());
A = int(input());
B = int(input());

i = A+1;
menor = 0;
maior = 0;

while i<=B:
    temp_soma = 0;
    for j in range(0,len(str(i))):
        temp_soma += int(str(i)[j]);
    if menor==0 and temp_soma==soma:
        menor = i;
    if temp_soma==soma and i>maior:
        maior = i;
    i+=1;
print(menor);
print(maior);