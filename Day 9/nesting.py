capitals = {
    "France": "Paris",
    "Italy": "Rome",
    "Monetengro": "Podgorica"
}

# Nested list in the dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Italy": ["Rome", "Milano", "Firenze"],
#     "Montenegro": ["Podgorica", "Cetinje", "Budva"]
# }

# print Lille


nested_list = ["a", "b", ["c", "d"]]
print(nested_list[2][1])

travel_log = {
    "France": {
        "num_times_visit": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Italy": {
        "num_times_visit": 4,
        "cities_visited": ["Rome", "Firenze"]
    },
    "Montenegro": {
        "num_times_visit": 2,
        "cities_visited": ["Podgorcia"]
    },
}

print(travel_log["Italy"]["cities_visited"][1])