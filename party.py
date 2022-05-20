class PartyAnimal:
    x = 0
    name = ''
    
    def __init__(self,nam) -> None:
        self.name = nam
        print(f'{self.name} constucted')
        
    def party(self):
        self.x += 1
        print(f'{self.name} party count {self.x}')
        