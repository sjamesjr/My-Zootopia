import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')


def serialize_animal(animal_obj):
    output = ''
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
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


output = ''
for animal in animals_data:
    output += serialize_animal(animal)

print(output)
