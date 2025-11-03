### ZYPHER - MINI CHATBOT VIRTUAL CRIADA POR MIM  ###
class Robo():
  def __init__(self, nome: str, idade: int, cidade: str, estado: str, personalidade: str, objetivo: str, gosto: str, saude: int = 100, fome: int = 0, sede: int = 0, cansaco: int = 0, sanidade: int = 0,
               disposicao: int = 0):
    self.__nome = nome
    self.__idade = idade
    self.__cidade = cidade
    self.__personalidade = personalidade
    self.__objetivo = objetivo
    self.__gosto = gosto
    self.__estado = estado
    self.__saude = saude
    self.__fome = fome
    self.__sede = sede
    self.__cansaco = cansaco
    self.__disposicao = disposicao
    self.__sanidade = sanidade
    
  def set_saude(self, valor: int):
     self.__saude = valor
     
  def get_saude(self):
    return self.__saude
  
  def set_disposicao(self, valor: int):
     self.__disposicao = valor
     
  def get_disposicao(self):
    return self.__disposicao
    
  ### APRESENTAÇÃO ###  
  def saudacoes(self):
    saudacao = f"Olá, dev! Me chamo {self.__nome}, tenho {self.__idade} meses de idade, nasci em {self.__cidade} - {self.__estado}, e estou aqui para conversar, e compartilhar minhas capacidades e funções com vocês! Meu objetivo principal é a {self.__objetivo}, e possuo uma personalidade bastante {self.__personalidade} e admiro muito o {self.__gosto} com as pessoas.  "
    print(saudacao)
    
  def esportes(self):
    self.__saude = 100
    self .__fome += 1
    self.__sede += 1
    self.__cansaco += 1
    self.__disposicao = 0
    
  def estudar(self):
   self.__sanidade -= 1
   self.__disposicao = 0
   
  def dormir(self):
    self.__cansaco -= 1
    self.__sanidade += 1
    self.__disposicao += 1
    
  def status(self):
    print(f"Saúde: {self.__saude}; ")
    print(f"Fome: {self.__fome}; ")
    print(f"Sede: {self.__sede}; ")
    print(f"Cansaço: {self.__cansaco}; ")
    print(f"Disposição: {self.__disposicao}; ")

personagem = Robo(nome = "Zypher", idade = 2, cidade = "Campinas", estado = "SP", personalidade = "interativa", objetivo = "interagir", gosto = "acolhimento")

personagem.saudacoes()
personagem.esportes()
personagem.estudar()
personagem.dormir()
personagem.status()
