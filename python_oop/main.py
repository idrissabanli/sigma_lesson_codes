

class Person:
    __age = 0 # private
    _working_time = '09:00-18:00' # protected

    def __init__(self, first_name, last_name):
        self.name = first_name # public
        self.surname = last_name

    def __str__(self):
        return f'{self.name} {self.surname} Age: {self.__age}'

    @property
    def age(self): # getter
        return self.__age

    @age.setter
    def age(self, value): # setter
        if value <= self.__age or value > 150:
            raise Exception
        self.__age = value


class Empoloyee(Person):
    _working_time = '10:00-19:00'

    def __init__(self, first_name, last_name, department):
        super().__init__(first_name=first_name, last_name=last_name)
        self.department = department

    def __str__(self):
        return f'{self.name} {self.surname} Department: {self.department}'

idris = Empoloyee('Idris', 'Shabanli', 'IT')

print(idris)



# print(idris._working_time)
# print(idris.age)
# idris.age += 20
# idris.age += 220
# print(idris.age)


# # idris.age = 220

# # print(idris)

# class B:
#     def sound(self):
#         print('bbbbbbbbb')

# class A:
#     def sound(self):
#         print('ffffff')

# class Animal(A):

#     def sound(self):
#         print('uuuuuuu')


# class Dog(Animal, A, B):
    
#     def sound(self): # override
#         print('Bow bow')
#         super(Dog, self).sound()

# a = Dog()
# a.sound()

# class UpdateProfile(LoginRequired, UpdateView):
#     model = User
