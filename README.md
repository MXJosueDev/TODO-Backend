# TODO's Backend APP

Simple backend application for serving [TODO's Web](https://github.com/MXJosueDev/todo-web), written in Python using Django and Django REST Framework.

Note: Do not use this app for serious purposes. This project is used only to help me improve my skills in Fullstack Web Development.

## Features

-   Create and update Lists
-   Create, update, and delete TODO items
-   JSON responses for easy API consumption
-   OpenAPI 3.0 specifications
-   Swagger Documentation
-   Redoc Documentation

# API Docs

-   [Swagger](https://todo-backend-mxjosuedev.vercel.app/api/docs/)
-   [Redoc](https://todo-backend-mxjosuedev.vercel.app/api/redoc/)

# Local installation

To set up the project locally, follow these steps:

1. **Clone the repository:**

    ```sh
    git clone https://github.com/MXJosueDev/todo-backend.git
    cd todo-backend
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Copy the sample environment file and update it with your configuration:

    ```sh
    cp .env.sample .env
    ```

    Edit the `.env.` file to set your environment variables.

5. **Apply the database migrations:**

    ```sh
    python manage.py migrate
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

    The application will be available at `http://127.0.0.1:8000/`.

7. **Access the API documentation:**

    - [Swagger](http://127.0.0.1:8000/api/docs/)
    - [Redoc](http://127.0.0.1:8000/api/redoc/)

# Usage

You are free of use this work under the [MIT License](/LICENSE)
