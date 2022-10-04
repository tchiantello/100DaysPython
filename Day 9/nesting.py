#nest things within a dictionary

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#nest list in a dictionary
#eg a travel log of locations you've visited in a country
travel_log = {
    "France": ["Paris", "Lillie", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#nest a dictionary in a dictionary
#update a travel log with how many times I've visited or label the data
travel_log = {
    "France": {"cities_visited": ["Paris", "Lillie", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 0},
    "Japan": {"cities_visited": ["Tokyo", "Osaka", "Kyoto", "Shingu", "Nara"], "total_visits": 3}
}

#nesting dictionaries inside of lists
travel_log = [
    {
    "country": "France",
    "cities_visited": ["Paris", "Lillie", "Dijon"],
    "total_visits": 12
    },
    {
    "country": "Germany", 
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 0
    },
]