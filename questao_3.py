import json

with open("dados.json") as dados:
    data = json.load(dados)

lista_valor = []
lista_valor_sem_nulo = [] # Lista de valores sem os valores iguais a 0.
soma_valores = 0  # Soma do faturamento de todos os dias
quantdias_com_faturamento = 0  # Quantidade de dias em que o faturamente é diferente de 0.
quantdias_fat_maior = 0 # Quantidade de dias em que o faturamente é maior q o faturamento mensal.


for i in data:
    if (i["valor"] != 0):
        lista_valor_sem_nulo.append (i ["valor"])
    if (i ["valor"] != 0 ):
        quantdias_com_faturamento += 1
    lista_valor.append (i ["valor"])
    soma_valores = soma_valores + i ["valor"]

media_fatmensal = soma_valores/quantdias_com_faturamento # média do faturamento mensal

for i in data:
    if(i ["valor"] > media_fatmensal):
        quantdias_fat_maior += 1


max_faturamento = max(lista_valor)
min_faturamento = min(lista_valor_sem_nulo)

print (f"\nO maior faturamento do mes foi {max_faturamento}")
print (f"\nO menor faturamento do mes foi {min_faturamento}")
print (f"\nA quantidade de dias em que o faturamento foi maior que o faturamento mensal é: {quantdias_fat_maior}")