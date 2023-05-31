resultado = int(input());
lista_registros = [];

for i in range(0,resultado):
    registros = input();
    for j in range(0,len(registros)):
        if registros[j] == ' ':
            lista_registros.append(registros[0:j]);
            lista_registros.append(int(registros[j+1:len(registros)]));
            break;
print(lista_registros);
i = 1;
espera = 0;
jafoi = [];
while i <= len(lista_registros)-1:
    state = 0;
    espera = 0;
    zera = 0;
    if lista_registros[i-1] != 'E' and lista_registros[i-1] != 'T' and lista_registros[i] not in jafoi:
        j = i+2;
        while j <= len(lista_registros)-1:
            if lista_registros[j-1] == 'T':
                espera += lista_registros[j];
            elif lista_registros[i] != lista_registros[j]:
                espera += 1;
            elif lista_registros[i-1] == lista_registros[j-1] and lista_registros[i-1]=='R':
                state = 1;
            else:
                if state == 1:
                    jafoi.append(lista_registros[i])
                    break;
                else:
                    break;

            j+=2;
    if state == 0 and (lista_registros[i-1] != 'E' and lista_registros[i-1]!='T'):
        print(-1);
    elif espera>0:
        print(lista_registros[i], espera);
    i+=2;

#['R', '1', 'R', '2', 'T', '4', 'E', '1', 'E', '2']