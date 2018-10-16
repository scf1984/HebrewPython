# bob = ['Bob', 'Marshall', 1995]
# alice = ['Alice', 'Chain', 1998]

# print(alice[0] + ' ' + alice[1])
# print(f'{bob[0]} {bob[1]}')

import datetime

class Person:
    def __init__(self, first_name, last_name, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def age(self):
        return datetime.datetime.now().year - self.birth_year

    def greet(self, other):
        return f'{self.first_name} says hello to {other.first_name}'

bob = Person('Bob', 'Marshall', 1995)
alice = Person('Alice', 'Chain', 1998)
print(bob.greet(alice))
