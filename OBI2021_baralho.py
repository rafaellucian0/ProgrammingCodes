copas = []; copas_count = 0;
espadas = []; espadas_count = 0; 
ouros = []; ouros_count = 0;
paus = []; paus_count = 0;
cartas = input("");
count_repetidas = 0;

def repetidas(conjunto, contador):
    count_repetidas = 0;
    for i in range(0,contador-1):
        for j in range(i, contador-1):
            if i!=j and conjunto[i]==conjunto[j]:
                count_repetidas+=1;
    if count_repetidas>0:
        return 1;
    else:
        return 0;                

def analisa_Conjuntos(conjunto, contador):
    if repetidas(conjunto,contador)==1:
        print("erro");
    elif contador==13:
        print(0);
    else:
        print(13-contador-count_repetidas);

i = 0;

while i<len(cartas)-2:
    if cartas[i+2]=='C':
        copas.append(cartas[i:i+2]);
        copas_count+=1;
    
    elif cartas[i+2]=='E':
        espadas.append(cartas[i:i+2]);
        espadas_count+=1;
    
    elif cartas[i+2]=='U':
        ouros.append(cartas[i:i+2]);
        ouros_count+=1;
    
    elif cartas[i+2]=='P':
        paus.append(cartas[i:i+2]);
        paus_count+=1;
    else: break;
    i+=3;

analisa_Conjuntos(copas,copas_count);
analisa_Conjuntos(espadas,espadas_count);
analisa_Conjuntos(ouros,ouros_count);
analisa_Conjuntos(paus, paus_count);