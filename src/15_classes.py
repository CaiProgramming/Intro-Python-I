# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat,lon):
        self.lat = lat
        self.lon = lon
    def __str__(self):
        return 'lat: ' + str(self.lat),"lon: " + str(self.lon)
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
latlon = LatLon("10","-126");
print(latlon.__str__())
class Waypoint(LatLon):
    def __init__(self,name,lat,lon):
        super().__init__(lat, lon)
        self.name = name
    def __str__(self):
        superstr = super().__str__()
        return 'name: ' + self.name, str(superstr)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    pass
    def __init__(self,name,difficulty,size,lat,lon):
        super().__init__(name,lat,lon)
        self.difficulty = difficulty
        self.size = size
    def __str__(self):
        superstr = super().__str__()
        return 'difficulty: ' + str(self.difficulty),'size: ' + str(self.size),str(superstr)
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
way = Waypoint("Catacombs",10,-120)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(way.__str__())

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
print(geocache.__str__())
