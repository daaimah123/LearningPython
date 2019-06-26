class Human: 
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    def __repr__(self):
        return f'Human name {self.first} {self.last}.'
    def __len__(self):
        return self.age
    def __add__(self,other):
        if isinstance(other, Human):
            return Human(first='newborn', last=self.last, age=0)
        return 'You cant add that'
    def __mul__(self, other):
        if isinstance(other, int):
            return [self for i in range(other)]
        return 'cant multiply'

human1 = Human('Daaimah', 'Tibrey', 26)
human2 = Human('Pete', 'The Cat', 28)
print(human1)
print(f'length is : {len(human1)}')
print(human2 + human1)
print(human1 * 2)