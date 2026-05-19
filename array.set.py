'''Array & Set
(1) Array 
(2) Set
(3) Specific operators with set
'''


from array import array
print("==== Array ===")
# integer, float
# Katta hajmdagi sonlar bn ishlayotganimizdagina arraylardan foydalanamiz va array strict type
numbers = array("i", [1, 2, 3, 4, 5, 7, 8, 19])
print("numbers(1)", numbers)


numbers.append(100)
numbers.insert(0, 14)
print("numbers(2)", numbers)

numbers.remove(5)
numbers.pop()
print("numbers(3)", numbers)


del numbers[0:2]
print("numbers(4)", numbers)


print("==== Set ===")

# {Set} of unique collection without keeping order! takroriy sonlardi faqat birmarta qabul qiladi tartib yoq

new_numbers = array("i", [1, 2, 3, 4, 5, 4, 7, 5, 7, 8, 41])
numbs_set = set(new_numbers)

print(f"the numbs_set: {numbs_set} and type: {type(numbs_set)}")

numbs_set.add(200)
print("numbs_set(1):", numbs_set)

numbs_set.add(7)
print("numbs_set(2):", numbs_set)


print("====  Specific operators with set ===")

# | & - ^

a = {10, 20, 50}
b = {20, 40}

result1 = a | b  # union
result2 = a & b  # intersection
result3 = a - b  # difference
result4 = a ^ b  # symmetric difference bir birida qatnashmaganlarni topledi


print("result1:", result1)
print("result2:", result2)
print("result3:", result3)
print("result4:", result4)
