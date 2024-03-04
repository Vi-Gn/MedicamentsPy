import sys

class Car:
  instances = []
  
  def __init__(self, name: str, horsePower: int) -> None:
    self.name = name
    self.horsePower = horsePower
    
    Car.instances.append(self)
    
  def __del__(self):
    print(f"Car named : {self.name} is being destroyed")
    
    
Audi = Car('rs6', 800)

# ref count nous donne ici 3 on a la ref dans la var "Audi", Car.instances"[0]" et la troisieme pour la var passer par la fonction sys.getrefcount("Audi")
print(f"on a : {sys.getrefcount(Audi)} references d'object Audi")

del Audi

print(f"on a : {sys.getrefcount(Car.instances[0])} references d'object Audi apres del de ref de la var Audi")

print(Car.instances[0].name)

del Car.instances[0]

input()