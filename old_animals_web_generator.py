import json


def load_data(file_path):
    """Loads data from a JSON file.

    Args:
        file_path (str): The path to the JSON file to load.

    Returns:
        dict: The loaded JSON data.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


# Load data from JSON file
animals_data = load_data('animals_data.json')


def print_animal_info(animals_data):
    """Generates HTML for each animal's information.

    Iterates through the provided data and constructs HTML list items
    containing the name, diet, type, and primary location of each animal.

    Args:
        animals_data (list): A list of dictionaries, each representing an animal.

    Returns:
        str: The generated HTML content for each animal.
    """
    output = ''  # Initialize an empty string to accumulate HTML content

    for animal in animals_data:
        # Append the name and characteristics of each animal to the output string
        output += '<li class="cards__item">'
        output += f'<div class="card__title"> {animal["name"]}</div>\n'
        output += '  <p class="card__text">\n'
        output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"

        # Check if 'type' exists in characteristics; if not, add a placeholder
        if 'type' in animal['characteristics']:
            output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"
        else:
            output += "<strong>Type:</strong> N/A <br/>\n"

        # Add the first location associated with the animal
        output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"
        output += '</p>\n'
        output += '</li>'

    return output


# Open the template file and replace the placeholder with generated animal info
with open("animals_template.html", "r") as file:
    content = file.read()
    animal_info = print_animal_info(animals_data)
    new_content = content.replace("__REPLACE_ANIMALS_INFO__", animal_info)

# Write the updated content to a new HTML file
with open("animals.html", "w") as file2:
    file2.write(new_content)
    print("Website was successfully generated to the file animals.html.")
