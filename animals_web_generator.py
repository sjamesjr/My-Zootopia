import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')


def print_animal_info(animals_data):
    """Iterates through the animals and prints Name, Diet, first location, and Type if they exist."""
    output = ''  # define an empty string
    for animal in animals_data:
        # append information to each string
        output += '<li class="cards__item">'
        output += f'<div class="card__title"> {animal['name']}</div>\n'
        output += '  <p class="card__text">\n'
        output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"
        if 'type' in animal['characteristics']:
            output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"
        else:
            output += "<strong>Type:</strong> N/A <br/>\n"  # Add a placeholder if 'type' is missing
        output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"
        output += '</p>\n'
        output += '</li>'

    return output


with open("animals_template.html", "r") as file:
    content = file.read()
    animal_info = print_animal_info(animals_data)
    new_content = content.replace("__REPLACE_ANIMALS_INFO__", animal_info)

print(new_content)
