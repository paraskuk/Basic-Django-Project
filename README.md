# DjangoProject

This is a simple Django project with two views: `HelloView` and `HelloRoot`.

## Requirements

- Python 3.x
- Django 3.x or later

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd DjangoProject
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the Django development server:
    ```sh
    python manage.py runserver
    ```

## Usage

- Access the `HelloView` at [http://127.0.0.1:8000/hello/](http://127.0.0.1:8000/hello/)
- Access the `HelloRoot` at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Project Structure

- `DjangoProject/urls.py`: URL configuration for the project.
- `DjangoProject/views.py`: Contains the `HelloView` and `HelloRoot` views.

## License

This project is licensed under the MIT License.