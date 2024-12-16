# Django Project

This is a Django-based web application designed to manage and track book distribution expenses. The application allows users to input and view distribution records, manage book categories, and visualize expense data through interactive charts.

## Features

- **Book Management**: Add, edit, and view books in different categories.
- **Expense Tracking**: Record distribution expenses and categorize them for easy tracking.
- **Custom Admin Interface**: Built using Django Admin for easy management of books and expenses.
- **Data Visualization**: Expense data is visualized using interactive charts with **Chart.js**.
- **User-friendly Front-end**: The application is responsive and built using **HTML5, CSS3**, and **JavaScript**.

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML5, CSS3, JavaScript
- **Data Visualization**: Chart.js
- **Version Control**: Git, GitHub
- **Development Environment**: Visual Studio Code

## Setup and Installation

### Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Django
- Git

### Installation Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/django-project.git
    ```
2. Navigate to the project directory:
    ```bash
    cd django-project
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Apply migrations to set up the database:
    ```bash
    python manage.py migrate
    ```
5. Create a superuser to access the Django admin interface:
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create the user.
    
6. Run the development server:
    ```bash
    python manage.py runserver
    ```
7. Open your browser and navigate to:
    ```
    http://127.0.0.1:8000
    ```
    You can also access the **Django Admin** at:
    ```
    http://127.0.0.1:8000/admin
    ```
## Project Structure

- `book_distribution/`: The main Django project directory.
    - `settings.py`: Configuration settings for the project.
    - `urls.py`: URL routing for the application.
    - `wsgi.py`: WSGI configuration for deployment.
- `books/`: The app responsible for managing book data and expenses.
    - `models.py`: Defines the database models for books and expenses.
    - `views.py`: Views to handle user requests.
    - `admin.py`: Custom admin interface for managing records.


