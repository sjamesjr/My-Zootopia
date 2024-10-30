import IPython
import requests
import json

#
#
# def load_data(file_path):
#     """ Loads a JSON file """
#     with open(file_path, "r") as handle:
#         return json.load(handle)
#
#
# animals_data = load_data('animals_data.json')


def serialize_animal(animal_obj):
    output = ''
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    output += f"<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>\n"
    if 'type' in animal_obj['characteristics']:
        output += f"<strong>Type:</strong> {animal_obj['characteristics']['type']}<br/>\n"
    else:
        output += "<strong>Type:</strong> N/A <br/>\n"  # Add a placeholder if 'type' is missing
    output += f"<strong>Location:</strong> {animal_obj['locations'][0]}<br/>\n"
    output += '</p>\n'
    output += '</li>'

    return output


def main():
    user_input = input("Enter the name of an animal: ")
    url = "https://api.api-ninjas.com/v1/animals"
    params = {"name": {user_input}}
    header = {"X-Api-Key": "L/K6XFChAP081dYR34/DsA==49HJZUygpquvzVDn"}
    response = requests.get(url, params=params, headers=header)
    data = response.json()

    serial_output = ''
    for animal in data:
        serial_output += serialize_animal(animal)

    with open("animals_template.html", "r") as file:
        content = file.read()
        new_content = content.replace("__REPLACE_ANIMALS_INFO__", serial_output)

    with open("animals.html", "w") as file2:
        file2.write(new_content)
    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
