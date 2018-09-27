# Implementation of Person class


#################################################
# Student adds code where appropriate

# definition of Person class
class Person:
    
    def __init__(self, first, last, year):
        self.first_name = first
        self.last_name = last
        self.birth = year
        
    def full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def age(self, current_year):
        return current_year - self.birth
    
    def __str__(self):
        return "The person's name is " + self.full_name() + '. Their birth year is ' + str(self.birth)
 
    
#################################################
# Student adds code where appropriate    
    
# implementation of average_age
def average_age(person_list, current_year):
    total = .0
    for person in person_list:
        total += person.age(current_year)
    return total / len(person_list)
###################################################
# Testing code

joe = Person("Joe", "Warren", 1961)
john = Person("John", "Greiner", 1966)
stephen = Person("Stephen", "Wong", 1960)
scott = Person("Scott", "Rixner", 1987)  

print joe
print john
print stephen
print scott

print joe.age(2013)
print scott.age(2013)   # yeah, right ;)
print john.full_name()
print stephen.full_name()

instructors = [joe, john, stephen, scott]
print average_age(instructors, 2013)

instructors.pop() # get rid of Scott and his bogus age
print average_age(instructors, 2013)

####################################################
# Output of testing code - results of __str__ method may vary

#The person's name is Joe Warren. Their birth year is 1961
#The person's name is John Greiner. Their birth year is 1966
#The person's name is Stephen Wong. Their birth year is 1960
#The person's name is Scott Rixner. Their birth year is 1987
#52
#26
#John Greiner
#Stephen Wong

####################################################
# Output of testing code

#44.5
#50.6666666667
