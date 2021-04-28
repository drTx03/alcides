print ('EM QUEM APOSTAR?')
time1 = input ('Nome do time 1: ')
vitorias1 = int(input('Número de vitórias nas últimas 5 partidas: '))
gols_pro1 = int(input('Número de gols feitos do time nas últimas 5 partidas: '))
gols_sofridos1 =  int(input('Número de gols sofridos nas últimas 5 partidas: '))
home1= int(input('Número de vitórias nas últimas 5 partidas em casa: '))
gols_home1= int(input('Número de gols nos ultimos 5 jogos em casa: '))
gols_sof_home1 = int(input('Digite o número de gols sofridos por esse time em casa nos últimos 5 jogos'))

result_vitoria1= (vitorias1/5)
result_vitoria1= (result_vitoria1*100)
media_gol1= (gols_pro1/5)
media_gols_sofridos1= (gols_sofridos1/5)
media_pro_sofridos1= float (gols_pro1/gols_sofridos1)
vit_home1= (home1/5)
vit_home1= (vit_home1*100)
media_gols_home1= (gols_home1/5)
media_gols_sof_home1=  (gols_sof_home1/5)
media_pro_sofridos_h1= (gols_home1/gols_sof_home1)


time2 = input ('Nome do time 2: ')
vitorias2 = int(input('Número de vitórias nas últimas 5 partidas: '))
gols_pro2 = int(input('Número de gols feitos do time nas últimas 5 partidas: '))
gols_sofridos2 =  int(input('Número de gols sofridos nas últimas 5 partidas: '))
home2= int(input('Número de vitórias nas últimas 5 partidas em casa: '))
gols_home2= int(input('Número de gols nos ultimos 5 jogos em casa: '))
gols_sof_home2 = int(input('Digite o número de gols sofridos por esse time em casa nos últimos 5 jogos'))

result_vitoria2= (vitorias2/5)
result_vitoria2= (result_vitoria2*100)
media_gol2= (gols_pro2/5)
media_gols_sofridos2= (gols_sofridos2/5)
media_pro_sofridos2=  float(gols_pro2/gols_sofridos1)
vit_home2= (home2/5)
vit_home2= (vit_home2*100)
media_gols_home2= (gols_home2/5)
media_gols_sof_home2= (gols_sof_home2/5)
media_pro_sofridos_h2= (gols_home2/gols_sof_home2)

if result_vitoria1 > result_vitoria2:
    vencedor= time1
if result_vitoria2 > result_vitoria1:
    vencedor= time2
if result_vitoria1==result_vitoria2:
    vencedor=(str('empate'))
    
print('                  ')
print('### RELATÓRIO DO ',time1,'###')
print('A média de vitórias do ' ,time1, 'é de ',result_vitoria1,'%')
print('A média de gols do',time1, 'é de ' ,media_gol1,'gols')
print('A média de gols sofridos pelo',time1, 'é de ',media_gols_sofridos1,'gols')
print('O ',time1, 'faz',round (media_pro_sofridos1,2), 'gols a cada gol sofrido')
print('                      ')
print('### RELATÓRIO DO ',time1,'DENTRO DE CASA ###')
print('A média de vitórias do ' ,time1, 'em casa é de ',vit_home1,'%')
print('A média de gols do',time1, 'em casa é de ' ,media_gols_home1,'gols')
print('A média de gols sofridos pelo',time1, 'em casa é de ',media_gols_sof_home1,'gols')
print('O ',time1, 'faz',round(media_pro_sofridos_h1,2), 'gols a cada gol sofrido em casa')
print('         ')
print('###############################################')
print('         ')

print('### RELATÓRIO DO ',time2,'###')
print('A média de vitórias do ' ,time2, 'é de ',result_vitoria2,'%')
print('A média de gols do',time2, 'é de ' ,media_gol2,'gols')
print('A média de gols sofridos pelo',time2, 'é de ',media_gols_sofridos2,'gols')
print('O ',time2, 'faz',round(media_pro_sofridos2,2), 'gols a cada gol sofrido')
print('                      ')
print('### RELATÓRIO DO ',time2,'DENTRO DE CASA ###')
print('A média de vitórias do ' ,time2, 'em casa é de ',vit_home2,'%')
print('A média de gols do',time2, 'em casa é de ' ,media_gols_home2,'gols')
print('A média de gols sofridos pelo',time2, 'em casa é de ',media_gols_sof_home2,'gols')
print('O ',time2, 'faz',round(media_pro_sofridos_h2,2), 'gols a cada gol sofrido em casa')
print('         ')
print('###############################################')
print('       ')
total_prob= result_vitoria1 + result_vitoria2
total_prob= total_prob/100
chance1= result_vitoria1/total_prob
chance2= result_vitoria2/total_prob

print('O provável vencedor da partida entre ',time1,'X',time2,'desconsiderando o critério de mandante é: ',vencedor,)
print('A probabilidade de vitória de',time1, 'é de' ,round(chance1,2),'%')
print('A probabilidade de vitória de',time2, 'é de' ,round(chance2,2),'%')
if media_pro_sofridos1>media_pro_sofridos2:
    print('Um possível placar cheio da partida seria de')
    print(int(media_pro_sofridos1)), 'X' ,(int(media_pro_sofridos2))
if media_pro_sofridos2>media_pro_sofridos1:
    print('Um possível placar cheio da partida seria de')
    print(int(media_pro_sofridos2)), 'X' ,(int(media_pro_sofridos1))
