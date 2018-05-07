class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.people_greeted = []
        self.friends = []
        self.greeting_count = 0
        self.unique_greetings = 0

    def __repr__(self):
        return (self.name, self.email, self.phone)


    def greet(self, other_person):
        print('Hello %s, I am %s!' % (other_person.name, self.name))
        self.greeting_count +=1
        if other_person.name not in self.people_greeted:
            self.people_greeted.append(other_person.name)
            self.unique_greetings +=1

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")

    def add_friend(self, new_friend):
        self.friends.append(new_friend)
        print("new friends can't triforce")

    def num_friends(self):
        return(len(self.friends))

    def num_unique_people_greeted(self):
        return self.unique_greetings

sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')

jordan = Person('Jordan','jordan@aol.com','495-586-3456')

sonny.greet(jordan)

jordan.greet(sonny)
jordan.greet(sonny)
jordan.greet(sonny)
jordan.greet(sonny)

print(jordan.greeting_count)
print(jordan.num_unique_people_greeted())

sonny.print_contact_info()

jordan.add_friend(sonny)
sonny.add_friend(jordan)

jordan.num_friends()

print(sonny.num_unique_people_greeted())

print(jordan.__repr__())

print(f"{sonny.name} and {sonny.email}")
print(f"{jordan.name} and {jordan.email}")
print(len(jordan.friends))

class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(f"{self.year} {self.make} {self.model}")

car = Vehicle('Nissan', 'Leaf', 2015)
car.print_info()
