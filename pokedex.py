import requests

# API Base URL
API_URL = "https://pokeapi.co/api/v2/pokemon/"

# Dictionary to store collected Pokémon
pokedex = {}

def search_pokemon(name):
    response = requests.get(f"{API_URL}{name.lower()}")
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"].capitalize(),
            "id": data["id"],
            "height": data["height"],
            "weight": data["weight"],
            "types": [t["type"]["name"] for t in data["types"]]
        }
    else:
        print("Pokémon not found.")
        return None

def add_pokemon(name):
    pokemon = search_pokemon(name)
    if pokemon:
        if pokemon["name"] in pokedex:
            print(f"{pokemon['name']} is already in your Pokédex.")
        else:
            pokedex[pokemon["name"]] = pokemon
            print(f"{pokemon['name']} added to Pokédex.")

def view_pokedex():
    if pokedex:
        for name, details in pokedex.items():
            print(f"{name} - ID: {details['id']}, Height: {details['height']}, Weight: {details['weight']}, Types: {', '.join(details['types'])}")
    else:
        print("Your Pokédex is empty.")

def remove_pokemon(identifier):
    if identifier.isdigit():
        # Search by ID
        for name, details in list(pokedex.items()):
            if details["id"] == int(identifier):
                del pokedex[name]
                print(f"{name} (ID: {identifier}) removed from Pokédex.")
                return
        print(f"This Pokémon is not found in your Pokédex.")
    else:
        # Search by name
        name = identifier.capitalize()
        if name in pokedex:
            del pokedex[name]
            print(f"{name} removed from Pokédex.")
        else:
            print(f"Pokémon {name} not found in your Pokédex.")