# Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado o programa calcula o percentual de representação que 
# cada estado teve dentro do valor total mensal da distribuidora.

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es+ outros

rep_sp = (sp/total)*100
re_rj = (rj/total)*100
rep_mg = (mg/total)*100
rep_es = (es/total)*100
rep_outros = (outros/total)*100

print (f"\nO porcentual de representação que SP, RJ, MG, ES e outros estados tem são respectivamente: {rep_sp:,.2f}%, {re_rj:,.2f}%, {rep_mg:,.2f}%, {rep_es:,.2f}%, {rep_outros:,.2f}%.")
