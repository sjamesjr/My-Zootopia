import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')


def print_animal_info(animals_data):
    """Iterates through the animals and prints Name, Diet, first location, and Type if they exist."""
    for animal in animals_data:
        # Check if the 'name' field exists and print it
        if 'name' in animal:
            print(f"Name: {animal['name']}")
            if 'characteristics' in animal:
                characteristics = animal['characteristics']
                if 'diet' in characteristics:
                    print(f"Diet: {characteristics['diet']}")
                if 'type' in characteristics:
                    print(f"Type: {characteristics['type']}")
            if 'locations' in animal and animal['locations']:
                print(f"First Location: {animal['locations'][0]}")
            print()  # Print a newline for better readability between entries


print_animal_info(animals_data)
