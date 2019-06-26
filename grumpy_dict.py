class GrumpyDict(dict): 
    def dict__init__(self, dictionary):
        self.dictionary = dictionary

    def __missing__(self, key):
        print(f'key: {key} is not here')

    def __setitem__(self, key, value):
        print(f'change dictionary to: ')
        super().__setitem__(key, value)

d = GrumpyDict({'name':'Yoko', 'city': 'New York'})
print(d)
print(d['mom'])
d['mom'] = 'Daaimah'
print(d)