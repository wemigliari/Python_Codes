from object_function_city import City ### There is another filed in the folder named classes_objects

place1 = City("Barcelona", 1.6, "Spain", True)
place2 = City("Vingåker", 0.0015, "Sweden", False)
place3 = City("Stockholm", 2.2, "Sweden", True)

print(place1.name_ct)
print(place1.metro)
print(place3.population)

print(place1)
print(place2)
print(place3)

print(place3.metro_area())