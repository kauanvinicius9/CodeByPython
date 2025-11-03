def maior_elemento(lista):
  
  #Ver se a lista está vazia
  if not lista:
    return None
  
  #Assume que o primeiro elemento seja o maior
  maior = lista[0]
  
  #Percorrer a lista
  for elemento in lista:
    if elemento > maior:
      maior = elemento #Maior atualizado
      
  return maior