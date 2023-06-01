quilometros = int(input());
quilometros-=5; #3 quilometros do emissor, mais 2 de cada sensor
if quilometros % 8 == 1:#se resto = 1, sensor 1
    print(1);
elif quilometros % 8 == 2:#se resto = 2, sensor 3
    print(2);
elif quilometros % 8 == 3:#se resto = 2, sensor 3
    print(3);