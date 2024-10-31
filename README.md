# Animal Info Web Generator

This project generates a simple HTML webpage displaying information about animals. The program fetches animal data from an API and formats it into an HTML list, allowing users to view details such as the animal’s name, diet, type, and location.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/animal-info-web-generator.git
    cd animal-info-web-generator
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your API key:
    - Create a `.env` file in the project directory.
    - Add your API key to the `.env` file as follows:
      ```plaintext
      API_KEY=your_api_key_here
      ```

## Usage

To generate the animal info webpage:

1. Run the following command:
    ```bash
    python main.py
    ```
   
2. When prompted, enter the name of an animal. The program will retrieve data for that animal and generate an HTML file (`animals.html`) displaying the information.

3. Open `animals.html` in a web browser to view the generated webpage.

## Example

If you input `Lion` when prompted, the generated `animals.html` file might display:

- **Name**: Lion
- **Diet**: Carnivore
- **Type**: Mammal
- **Location**: Africa

If the animal does not exist in the data source, the output will display an error message in the HTML file.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes with clear descriptions.
4. Push the branch:
    ```bash
    git push origin feature-name
    ```
5. Submit a pull request, and describe your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
