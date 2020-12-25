class City:

    def  __init__(self, name_ct, population, country, metro):
        self.name_ct = name_ct
        self.population = population
        self.country = country
        self.metro = metro

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def metro_area(self):
        if self.metro > 0.5:
            return True
        else:
            return False