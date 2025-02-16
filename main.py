import pickle

''' INÍCIO MSORT ## 1 PARTE ## MSORT '''
''' INÍCIO  ANTERIOR - COMPARA OS ITENS SOLICITADOS NA ORDENAÇÃO '''

def anterior (x,y, dados): #Login Usuario1, Login Usuario2, Dicionario dados
  nomeX, seguidosX, seguidoresX, postsX = dados[x] #Buscando as demais informacoes no dicionario
  nomeY, seguidosY, seguidoresY, postsY = dados[y]

  if len(seguidoresX) > len(seguidoresY): return True
  if len(seguidoresX) < len(seguidoresY): return False

  if len(seguidosX) > len(seguidosY): return True
  if len(seguidosX) < len(seguidosY): return False

  if nomeX < nomeY: return True
  if nomeX > nomeY: return False

  if x < y: return True
  if x > y: return False

''' FIM  ANTERIOR - COMPARA OS ITENS SOLICITADOS NA ORDENAÇÃO '''

def msort(l, dados):
  if len(l) <= 1:
    return l
  else: 
    meio = len(l) // 2
    l1 = l[:meio]
    l2 = l[meio:]
    msort(l1, dados)
    msort(l2, dados)
    merge(l,l1,l2, dados)

  return (l) #Retornando apenas a lista. O dicionario j'a foi enviado anteriormente.

def merge(l, l1, l2, dados):
  i = 0
  j = 0
  k = 0

  while i < len(l1) and j < len(l2): 
    if anterior(l1[i], l2[j], dados): #ENVIANDO PARA A def ANTERIOR. Ela que ira comparar com os demais requisitos de ordenacao
      l[k] = l1[i]
      i += 1
    else:
      l[k] = l2[j]
      j += 1

    k += 1

  while i < len(l1):
    l[k] = l1[i]
    i += 1
    k += 1

  while j < len(l2):
    l[k] = l2[j]
    j += 1
    k += 1

''' FIM MSORT ## 1 PARTE ## MSORT '''

''' INÍCIO MSORT ## 2 PARTE ## MSORT '''
''' INÍCIO  ANTERIOR_FEED - COMPARA OS DADOS PARA ORDENAR OS POSTS DO FEED '''

def anteriorFeed(x,y): #Recebe X = (login, (nome_Foto, Comentario_Foto, (dia, mes, ano, hora, min))), Y = (login, (nome_Foto, Comentario_Foto, (dia, mes, ano, hora, min)))

  loginX, dadosPostsX = x #login, (nome_Foto, Comentario_Foto, (dia, mes, ano, hora, min))
  loginY, dadosPostsY = y

  nome_FotoX, comentario_FotoX, data_horaX = dadosPostsX #nome_Foto, Comentario_Foto, (dia, mes, ano, hora, min)
  nome_FotoY, comentario_FotoY, data_horaY = dadosPostsY

  diaX, mesX, anoX, horaX, minX = data_horaX #dia, mes, ano, hora, min
  diaY, mesY, anoY, horaY, minY = data_horaY
  
  # Ordena os Posts seguindo os criterios estabelecidos

  #Compara o ano
  if anoX > anoY:
      return True
  if anoX < anoY:
      return False
  #Compara o mes
  if mesX > mesY:
      return True
  if mesX < mesY:
      return False
  #Compara o dia
  if diaX > diaY:
      return True
  if diaX < diaY:
      return False
  #Compara a hora
  if horaX > horaY:
      return True
  if horaX < horaY:
      return False
  #Compara os min
  if minX > minY:
      return True
  if minX < minY:
      return False
  #Compara os logins
  if loginX < loginY:
      return True
  return False

''' FIM  ANTERIOR_FEED '''

def msortFeed(l): #MSort Utilizado para ordenar o feed
  if len(l) <= 1:
    return l
  else: 
    meio = len(l) // 2
    l1 = l[:meio]
    l2 = l[meio:]
    msortFeed(l1)
    msortFeed(l2)
    mergeFeed(l,l1,l2)

  return (l) #Retornando apenas a lista com os posts ordenados

def mergeFeed(l, l1, l2):
  i = 0
  j = 0
  k = 0

  while i < len(l1) and j < len(l2): 
    if anteriorFeed(l1[i], l2[j]): #ENVIANDO PARA A def anteriorFeed. - Ela e a responsavel por ordeenar seguindo os criterios estabelecidos
      l[k] = l1[i]
      i += 1
    else:
      l[k] = l2[j]
      j += 1

    k += 1

  while i < len(l1):
    l[k] = l1[i]
    i += 1
    k += 1

  while j < len(l2):
    l[k] = l2[j]
    j += 1
    k += 1

''' FIM MSORT ## 2 PARTE ## MSORT '''


''' PRIMEIRA PARTE UTILIZANDO MSORT ### MSORT '''

''' INICIO DEF MAIN '''

def main():
  #Abrindo o arquivo
  with open("./10/usuarios.bin", "rb") as f: #LOCAL DO ARQUIVO
    dados = pickle.load(f)
  #Arquivo fechado 

  ''' INICIO PRIMEIRA PARTE '''
  
  logins = [] #Lista que ira receber os logins
  
  for usuario in dados: #Para cada usuario na lista dados, logins.append(usuario). Ele se refere aos Logins
    logins.append(usuario) #Recebendo os logins fora de ordem
    
  logins = msort(logins, dados) #Enviando para o MSort os login, e o dicionario. Porem, a lista recebe somente os logins ordenados. Antes do msort retornar a lista, foi retirado o dicionario do return.
    
  for login in logins: #Para cada login dentro da lista
    nome, seguidos, seguidores, posts = dados[login]  #recebendo os demais dados do dicionario
    print('{} (segue {}, seguido por {})'.format(nome, len(seguidos), len(seguidores))) #Saida com as seguintes informacoes do usuario: Nome, Numero de seguidos e seguidores
  print('---')

  ''' FIM PRIMEIRA PARTE '''
  ''' INICIO SEGUNDA PARTE '''

  
  ''' SEGUNDA PARTE UTILIZANDO MSORT ### MSORT '''
  for login in logins: #Para cada login dentro da lista logins
    nome, seguidos, seguidores, posts = dados[login]  #recebendo os demais dados do dicionario
    print('Feed de {}:\n***'.format(nome)) #Iniciando o Feed do primeiro usuario
    
    lista_Feed = [] #Lista que ira receber o Feed de quem o usuario segue
    
    for loginSeguidoFeed in seguidos: #Selecionando o Login de cada pessoa seguida
      nomeFeed, seguidosFeed, seguidoresFeed, postsFeed = dados[loginSeguidoFeed] #Separando as informacoes do dicionario da pessoa seguida
      
      for postsPessoa in postsFeed: #Para cada Postagem feita pela pessoa seguida, estou adicionando na lista lista_feed
        lista_Feed.append((loginSeguidoFeed, postsPessoa))
        
    lista_Feed = msortFeed(lista_Feed) #Apos receber o Feed de todas as pessoas seguidas, ele manda para o mSortFeed, que ira ordenar o Feed
    
    for post_Seguido in lista_Feed: #Para cada post na lista_feed, ele ira criar o feed do usuario atual
      loginFeed, dadosPostsFeed = post_Seguido #Separando os dados da lista (login, (nome_Foto, comentario_Foto, (dia, mes, ano, hora, min)))
      nome_Foto, comentario_Foto, data_hora = dadosPostsFeed  # (nome_Foto, comentario_Foto, (dia, mes, ano, hora, min))
      diaFeed, mesFeed, anoFeed, horaFeed, minFeed = data_hora # (dia, mes, ano, hora, min)
      print('{}\n{}\n{}\n{}/{}/{}  {}:{}\n***'.format(loginFeed, nome_Foto, comentario_Foto, diaFeed, mesFeed, anoFeed, horaFeed, minFeed)) #Saida com as informacoes do Feed

  ''' FIM SEGUNDA PARTE '''

  return 0
if __name__ == '__main__': 
  main()

''' FIM DEF MAIN '''
