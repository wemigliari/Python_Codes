# We can use inheritance to import classes and functions from other classes

from inheritance_town import metropolitan_town_pop
from inheritance_city import metropolitan_city_pop

class city_town:

    def metro_town(self):
        print("Towns - Metropolitan town areas are territories under the threat of the conurbation phenomenon.")
    def pop_town(self):
        print("Towns - People menaced by an unbalanced distribution of wealth.")
    def cultural_town(self):
        print("Towns - Although dealing with two negative fronts, towns have a stronger cultural tissue.")
    def metro_city(self):
        print("Cities - Metropolitan areas are territories under the conurbation phenomenon.")
    def pop_city(self):
        print("Cities - People facing unbalanced distribution of wealth.")
