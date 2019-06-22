class User: 
    active_users = 0
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f'{self.first} has logged out'
    def full_name(self):
        return f'{self.first} {self.last}'
    def initials(self):
        return f'{self.first[0]}.{self.last[0]}.'
    def user_age(self):
        return  f'{self.age} years old'
    def likes(self, thing):
        return f'{self.first} {self.last} likes {thing}.'
user1 = User('Daaimah', 'Brown', 26)
user2 = User('Jahdai', 'Tibrey', 1)

# print(f'When I married, my name changed from {user1.first} {user1.last} to {user1.first} {user2.last}.')
# print(user1.likes('blueberry icecream topped with fresh mango cubes'))
# print(user1.initials() + ' is ' + user1.user_age())
print(user1.logout())