from inheritance_metropolitan import city_town

class mct1(city_town):
    def metro_town (self):
        print("Cambará")
    def village (self):
        print("Le droit à la ville by Henri Lefebvre")

mct2 = mct1()

mct2.metro_town()
mct2.village()
mct = city_town()
mct.pop_city()