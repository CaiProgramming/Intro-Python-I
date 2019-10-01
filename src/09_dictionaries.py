"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]


# Add a new waypoint to the list
# YOUR CODE HERE
waypoints.append({"lat":20,"lon":125,"name":"minecraft home"})
print(waypoints)
# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# YOUR CODE HERE

def FindAndModify(arr, str, chg):
    done = 0;
    for a in arr:
        if not done:
          for s in str.keys():
             for c in chg.keys():
                if a[s] == str[s]:
                    a[c] = chg[c]
                    done = 1;
                elif a[s] == chg[s]:
                    a[c] = chg[c]
                    done = 1;

        else:
            return a



print("changed:",FindAndModify(waypoints, {"name":'a place'} , {"name":"not a real place","lon":-130}));

print(waypoints)
# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE

for v in waypoints:
    for k in v:
        print("waypoint:",v,"keys:",k,"value:",v[k])
