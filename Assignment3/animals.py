class animals:
    def __init__(self):
        self.__eyes = 2 #private variable
        self._living = True #protected variable 
        self.legs = 4#Public variable

    def set_legs(self, legs):
        self.legs=legs
    def get_legs(self):
        return self.legs
    def eats(self):
        pass

class herbi(animals):
    def intestine(self):
        print("large size intestine")
    def eats(self):
        print("eat plants")
    def teeth(self):
        print("cananes are less developed")
    def number(self):
        print("more in number")
        
class carni(animals):
    def intestine(self):
        print("small size intestine")
    def eats(self):
        print("eat animals")
    def teeth(self):
        print("cananes are more developed")
    def number(self):
        print("small in number")
        
class oxen(herbi):
    def eats(self):
        herbi().eats()
        print("Eats leaves and grass")
        
class cow(oxen):
    def eats(self):
        oxen().eats()
    def feature(self):
        print("Gives milk with 4-5% fats")

class buffalo(oxen):
    def eats(self):
        oxen().eats()
    def feature(self):
        print("Gives milk with 10% fats")

class panthera(carni):
    def eats(self):
        carni().eats()
        print("Eats deers")

class lion(panthera):
    def eats(self):
        panthera().eats()
    def feature(self):
        print("King of Jungle")

class leopard(panthera):
    def eats(self):
        panthera().eats()
    def feature(self):
        print("Run Fast")

class cat(panthera, herbi):
    def eats(self):
        panthera().eats()
        herbi().eats()
    def feature(self):
        print("Domastic animal")
        
class canis(carni):
    def eats(self):
        carni().eats()
        print("leftovers of animals")

class dog(canis):
    def eats(self):
        canis().eats()
    def feature(self):
        print("are faithful")

class wolf(canis):
    def eats(self):
        canis().eats()
    def feature(self):
        print("are Cunning")

D = dog()
D.eats()
print()
C = cat()
C.eats()
