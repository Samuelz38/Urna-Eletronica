def candidatoVencedor():

  for c in range(len(info)):
    votos_bol = votos.count("22")
    votos_lul = votos.count("13")

  if votos_bol > votos_lul:
    print("Jair Bolsonaro venceu!")
  elif votos_lul > votos_bol:
    print("Lula venceu!")
  else:
    print("Os candidatos empataram!")

def zonaMaisVotada():

  maiorZona = 0
  qtdZona = 0

  for zon in range(1900, 1911):
    infozon = [zonas.count(str(zon)), zon]
    contagemzon.append(infozon)
  
  for c in range(11):
      
    if contagemzon[c][0] > qtdZona:
      maiorZona = contagemzon[c][1]
      qtdZona = contagemzon[c][0]
  
  print(f"A zona mais votada foi a {maiorZona}, com {qtdZona}")

def secaoMaisVotada():

  maiorSecao = 0
  qtdSecao = 0

  for sec in range(900, 911):
    infosec = [secao.count(str(sec)), sec]
    contagemsec.append(infosec)
  
  for c in range(11):
      
    if contagemsec[c][0] > qtdSecao:
      maiorSecao = contagemsec[c][1]
      qtdSecao = contagemsec[c][0]
  
  print(f"A zona mais votada foi a {maiorSecao}, com {qtdSecao}")

def sexoParticipativo():

  votos_masc = sexos.count("M")
  votos_fem = sexos.count("F")

  if votos_masc > votos_fem:
    print("Eleitores do sexo masculino compareceram mais nas eleições!")
  elif votos_fem > votos_masc:
    print("Eleitores do sexo feminino compareceram mais nas eleições!")
  else:
    print("Ambos os sexos compareceram igualmente nas eleições!")

num_candidato = "-2"
contagemzon = []
contagemsec = []
nomes = []
sexos = []
zonas = []
secoes = []
votos = []

while num_candidato != "-1":

  numcont = 0

  nome_cid = input("Digite o seu primeiro nome: ")
  nomes.append(nome_cid)

  print("M - Masculino")
  print("F - Feminino")
  sexo = input("Digite o seu sexo: ").upper()
  sexos.append(sexo)

  for zon in range(1900, 1911):
    print(f"{numcont + 1}: {zon}")
    numcont += 1
  
  zona = input("Escolha sua zona: ")
  zonas.append(zona)

  numcont = 0

  for sec in range(900, 911):
    print(f"{numcont + 1}: {sec}")
    numcont += 1
  
  secao = input("Escolha sua seção: ")
  secoes.append(secao)

  print("22 - Jair Bolsonaro")
  print("13 - Lula")
  num_candidato = input("Digite o número correspondente ao candidato: ")
  votos.append(num_candidato)

  if num_candidato != "-1":

    info = (nome_cid, sexo, zona, secao, num_candidato)

candidatoVencedor()

zonaMaisVotada()

secaoMaisVotada()

sexoParticipativo()


