programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."
                          }


# Adding new items to dictionary
programming_dictionary["loop"]="The action of doing something over and over again"

print(programming_dictionary)

# Create an empty dictionary
emptyDictionary={}
print(emptyDictionary)

# wipe an programming_dictionary
# programming_dictionary={}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"]="A moth in a computer"
print(programming_dictionary["Bug"])


# Loop through a dictionary
for key in programming_dictionary:
    print(f"{key} : {programming_dictionary[key]}")


#Nesting

capitals={
    "France":"Paris",
    "Germany":"Berlin"
}

#Nesting a Dictionary in a Dictionary

travel_log={
    "France": {"cities_visited":["Paris","Lille","Dijon"],"total_visits":12},
    "Germany":{"cities_visited":["Berlin","Humburg","Stuttgard "],"total_visits":5}
}

#Nesting Dictionary in a List

travel_log=[
    {
     "country": "France",
     "cities_visited": ["Paris","Lille","Dijon"],
     "total_visits": 12
    },
    {
     "country": "Germany",
     "cities_visited": ["Berlin","Humburg","Stuttgard"],
     "total_visits": 5
    }
]
