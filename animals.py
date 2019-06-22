class Pet:
    allowed = ['cat', 'dog', 'fish', 'horse', 'turtle']
    def __init__(self, name, species):
        self.name = name
        self.species = species
        if species not in self.allowed: 
            raise ValueError(f'You can\'t have a {species} as a pet!')
    def set_species(self, species):
        if species not in self.allowed: 
            raise ValueError(f'You can\'t have a {species} as a pet!')
        self.species = species

cat = Pet('Jet', 'cat')
dog = Pet('Wingdom', 'dog')
