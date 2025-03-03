from pokedex import * # Import Pokedex

def main():
    while True:
        print("\nPokédex Menu:")
        print("1. Search Pokémon")
        print("2. Add Pokémon to Pokédex")
        print("3. View Pokédex")
        print("4. Remove Pokémon")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter Pokémon name or ID: ")
            details = search_pokemon(name)
            if details:
                print(details)
        elif choice == "2":
            name = input("Enter Pokémon name to add: ")
            add_pokemon(name)
        elif choice == "3":
            view_pokedex()
        elif choice == "4":
            name = input("Enter Pokémon name to remove: ")
            remove_pokemon(name)
        elif choice == "5":
            print("Thank you for using Pokedex!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()