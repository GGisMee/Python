# 60__dictionary_comprehensions
# är som list comprehensions fast med dictionaries
def br(title):
    for i in range(0,2): print()
    print(title+":")

br("Changing")
cities_deg_F = {"New York":32, "Boston":75, "Los Angeles":100, "chicago":50}
cities_deg_C = {key: round(value-32*(5/9)) for (key,value) in cities_deg_F.items()}
print(cities_deg_C)

br("For loop")
weather = {"New York":"Snowing", "Boston":"sunny", "Los Angeles":"sunny", "chicago":"cloudy"}
for city in weather.keys():
    if weather.get(city) == "sunny":
        print(f"sunny in {city}")
    else:
        pass

print()

sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
print("sunny weather in "+str(sunny_weather.keys()).replace("dict_keys", "").replace("([", "").replace("])", "").replace("'",""))

br("if and for loop")
cities = {"New York":32, "Boston":75, "Los Angeles":100, "chicago":50}
desc_cities = {key: ("Warm" if value >= 40 else "Cold") for (key, value) in cities.items()}
print(desc_cities)

br("if and foor loop")
for city in cities:
    cities.update({city:"Warm"}) if cities.get(city) >= 40 else cities.update({city:"Cold"})
print(cities)


br("function")
def check_temp(value):
    if value >= 70:
        return "Hot"
    elif 69>= value >= 40:
        return("Warm")
    else:
        return("Cold")


cities_ = {"New York":32, "Boston":75, "Los Angeles":100, "chicago":50}
desc_cities_ = {key: (check_temp(value)) for (key, value) in cities_.items()}
print(desc_cities_)

