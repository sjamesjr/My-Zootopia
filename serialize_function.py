import data_fetcher



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
    data = data_fetcher.fetch_data(user_input)

    if data:
        serial_output = ''
        for animal in data:
            serial_output += serialize_animal(animal)
    else:
        serial_output = f'<h2>The animal "{user_input}" doesn\'t exist.</h2>'

    with open("animals_template.html", "r") as file:
        content = file.read()
        new_content = content.replace("__REPLACE_ANIMALS_INFO__", serial_output)

    with open("animals.html", "w") as file2:
        file2.write(new_content)
    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
