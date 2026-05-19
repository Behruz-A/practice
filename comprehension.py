'''Comphrehension
   (1) What is comphrehension
   (2) set and dictionary comp.
   '''

print("==== What is comphresion & list comphresion ===")
# Comphrehension acts like spread operator! spread operatorini bizga pythonda taqdim etadi


''' Comphrehension general syntax:
     a) *iterable
     b) <expression> for item in iterable
     c) <expression> for item in iterable <condition>
     '''

# list comp.
# comphrehension mantig'i numbers ni qiymatlaridan foydalangan holda butunlay yangi reference ga ega bolgan yangi listtimizni hosil qlishga yordam beradi
numbers = [1, 2, 3, 4, 5, 19]
list_numbers = [*numbers]  # a version
print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

print("=======")  # map, lambda bn qilgan ishn comp b version bn easy qildik
people = [("Ramos", 40), ("Vandek", 37), ("Khusanov", 22)]
list_people = [person[0] for person in people]  # b version


print("list_people:", list_people)


cars = [
    ("nexia", 78),
    ("cobalt", 88),
    ("zaparoj", 116),
    ("07 juguli", 109),
    ("malibu", 33)

]

list_cars = [car[0] for car in cars if car[1] > 80]  # c version
print("list_cars:", list_cars)
