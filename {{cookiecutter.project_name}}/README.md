# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Installation

To install {{ cookiecutter.project_name }}, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/{{ cookiecutter.author_name }}/{{ cookiecutter.project_name }}.git
   ```

2. Navigate to the project directory:
   ```
   cd {{ cookiecutter.project_name }}
   ```

3. Create a virtual environment and activate it:
   ```
   make venv
   source .venv/bin/activate
   ```

4. Install the dependencies:
   ```
   poetry install
   ```

## Usage

To use {{ cookiecutter.project_name }}, run the following command:

```
python -m {{ cookiecutter.module_name }}
```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

