"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {'North America': {'USA': ['Mountain View', 'Atlanta']}}
locations['Asia'] = {'India': ['Bangalore'], 'China':['Shanghai']}
locations['Africa'] = {'Egypt': ['Cairo']}

"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""
print '1'
city_list = locations['North America']['USA']
city_list.sort()
for city in city_list:
    print "{}".format(city)
    
print '2'
city_dict = locations['Asia']
city_list = []
for key, value in city_dict.iteritems():
    city_list.append("{} - {}".format(value[0], key))

city_list.sort()
for city in city_list:
    print "{}".format(city)
    
    
    
    