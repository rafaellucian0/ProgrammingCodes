n = int(input());
dario_count = 0;
xerxes_count = 0;
jogadas = {0: [1, 2], 1: [2, 3], 2:[3, 4], 3:[4, 0], 4: [0, 1] }
for i in range(0,n):
    jogada_atual = input();
    jogada_dario = jogada_atual[0];
    jogada_xerxes = jogada_atual[2];
    if int(jogada_dario) in jogadas[int(jogada_xerxes)]:
        xerxes_count+=1;
    else:
        dario_count+=1;
if dario_count>xerxes_count:
    print("dario");
else:
    print("xerxes");