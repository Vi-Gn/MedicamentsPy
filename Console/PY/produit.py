
class Produit:
  ## declaration des variables static et prive pour on peut stocker des info generale
  
  # stocker le dernier index inserer 
  __ref: int = 0
  
  # stocker le nombre des instances on a
  __count: int = 0
  
  
  def __init__(self, libelle: str, prix: float):
    # on l'ajoute d'une instance on increment le dernier index inserer par 1 et aussi combient des instances on a
    Produit.__ref += 1
    Produit.__count += 1
    ######################################################### Produits.append(self)
    ## declaration des vars d'instance
    # le ref va incrementer automatiquement par rappot a la var static __ref
    self.reference: int = Produit.__ref
    self.libelle: str = libelle
    self.prix:float = prix
    
    self.affiche(False)
    
    
  def __del__(self):
    ## don't la desctruction d'instance on va soustracter 1 dans le nombre des instances 
    ########################################################### try:
    ###########################################################   Produits.remove(self)
    ########################################################### except:
    ###########################################################   print(f"Product : {self.libelle} is already deleted from list")
    Produit.__count -= 1
    print('desctruction')
  
  def getCount(self):
    ## nombre d'instance actuel
    return (Produit.__count)
  
  def getLastRef(self):
    ## ref id de dernier instance creer 
    return (Produit.__ref)
  
  def affiche(self, shouldLog: bool = False):
    print(f"   Ref     : {self.reference}")
    print(f"   Libelle : {self.libelle}")
    print(f"   Prix    : {self.prix}")
    if shouldLog:
      self.log()
  
  def log(self):
    print(f"le nombre d'instance actuelle est de : {Produit.__count}")
    print(f"la ref du derniere element est : {Produit.__ref}")

# def GetProduits():
#   return Produits

# def CreeProduit(libelle: str, prix: float):
#   Produits.append(Produit(libelle, prix))

# def ClearProduits():
#   Produits
  
# # stocker une list qui contient des references pointers des objets pour les manipuler ulterieurement
# Produits: list[Produit] = []


# def LogAll():
#   print('--------------Log All-----------------')
  
#   if len(Produits) == 0:
#     print('--- There is nothing to log no instance has found')
#   for obj in Produits:
#     print('---')
#     obj.affiche(False)
    
#   print('--------------------------------------')
    
# def deleteAll():
#   print('------------delete All----------------')
  
#   for _ in range(Produit.__count):
#     print('---')
#     print(f"del item name : {Produits[-1].libelle}")
#     Produits[-1].deleteInst()
    
#   print('--------------------------------------')
      