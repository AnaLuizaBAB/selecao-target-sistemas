 # Informe um número de 1 a 1000 e verifique se ele pertence a sequência de Fibonacci
 
teste = int (input("\nInforme 0 numero inteiro, entre 0 e 1001, que deseja verificar se pertence a sequencia de Fibonacci: "))

termo_seguinte = 0
i = 0
lista = [0, 1] 

while (termo_seguinte < 1001):
   
  termo_seguinte = lista[i] + lista [i + 1]
  lista.append(termo_seguinte)
  
  i = i + 1


if (teste in lista):
  print ("\nO numero pertence a sequencia de Fibonacci.")
else:
  print ("\nO numero não pertence a sequencia de Fibonacci.")