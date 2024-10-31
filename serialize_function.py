import data_fetcher


def serialize_animal(animal_obj):
    """Generates HTML for a single animal's information.

    Creates an HTML list item displaying the name, diet, type, and primary
    location of the specified animal.

    Args:
        animal_obj (dict): Dictionary containing animal data.

    Returns:
        str: The HTML string for the animal's information.
    """
    output = ''  # Initialize an empty string to accumulate HTML content

    # Add animal name
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'

    # Add diet information
    output += f"<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>\n"

    # Add type information, or a placeholder if type is missing
    if 'type' in animal_obj['characteristics']:
        output += f"<strong>Type:</strong> {animal_obj['characteristics']['type']}<br/>\n"
    else:
        output += "<strong>Type:</strong> N/A <br/>\n"

    # Add primary location information
    output += f"<strong>Location:</strong> {animal_obj['locations'][0]}<br/>\n"
    output += '</p>\n'
    output += '</li>'

    return output


def main():
    """Main function to handle user input and generate HTML output.

    Prompts the user for an animal name, retrieves data for that animal using
    data_fetcher, and generates HTML output based on the retrieved data.
    """
    user_input = input("Enter the name of an animal: ")
    data = data_fetcher.fetch_data(user_input)

    # Check if data is returned and serialize it; otherwise, display an error message
    if data:
        serial_output = ''
        for animal in data:
            serial_output += serialize_animal(animal)
    else:
        serial_output = f'<h2>The animal "{user_input}" doesn\'t exist.</h2>'

    # Load HTML template and replace placeholder with serialized animal info
    with open("animals_template.html", "r") as file:
        content = file.read()
        new_content = content.replace("__REPLACE_ANIMALS_INFO__", serial_output)

    # Write the final content to an output HTML file
    with open("animals.html", "w") as file2:
        file2.write(new_content)
    print("Website was successfully generated to the file animals.html.")


# Execute main function if this file is run as a script
if __name__ == "__main__":
    main()
