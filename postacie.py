
import time
import os



class Postac:
      def __init__(self,name):
            self.name = name
            self.gold = 200
            self.alive = True
            
      def inf(self):
            print(f"""{self.name}\n {self.gold}\n {self.alive}""")
                        
            
      
class Mag(Postac):
      def __init__(self, name):
            super().__init__(name)
            self.hp = 100
            self.dps = 20
            
class Archer(Postac):
      def __init__(self, name):
            super().__init__(name)
            self. hp = 80
            self.dps = 20
            
class Warior(Postac):
      def __init__(self, name):
            super().__init__(name)
            self.hp = 110
            self.dps = 30
            
class Furas(Postac):
      def __init__(self, name):
            super().__init__(name)
            self.hp = 9000
            self.dps = 1
            
