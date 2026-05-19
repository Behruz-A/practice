'''Packages & Debugging
(1) Python packages & Core Package
(2) Package Manager & External Package
(3) Debugging
'''

import turtle
print("==== Python packages & Core Package ====")
''' Python Packages/Modules: Core, File, External
'''

# Core Packages > https://docs.python.org/3/library


# Core
t = turtle.Turtle()
t.shape()
t.speed(2)
t.circle(150)


turtle.done()


my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()

# with - Context Manager AVTOMATIK ravishda manabu ochilgan faylni oqib bolgach close amalini avtomatik ravishda ozi bajaradi
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)


print("DONE")
