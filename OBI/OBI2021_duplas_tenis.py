jogadores = [];

for i in range(0,4):
    nivel = int(input());
    jogadores.append(nivel);

for i in range(0,2):
    for j in range(0,2-i):
        if jogadores[j]>jogadores[j+1]:
            temp = jogadores[j];
            jogadores[j] = jogadores[j+1];
            jogadores[j+1] = temp;
        if jogadores[3-i] < jogadores[2-i]:
            temp = jogadores[3-i];
            jogadores[3-i] = jogadores[2-i];
            jogadores[2-i] = temp;

duplaUm = jogadores[0]+jogadores[3];
duplaDois = jogadores[1]+jogadores[2];

print(duplaUm-duplaDois)