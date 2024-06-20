# Task Management API

Welcome to the Task Management API, a FastAPI-based application designed to manage tasks efficiently. This API allows users to register, log in, and manage their tasks with features like creating, retrieving, and marking tasks as completed.

## Features

- User Registration
- User Login with JWT Authentication
- Create Tasks
- Retrieve Tasks
- Mark Tasks as Completed

## Technologies Used

- FastAPI
- Tortoise ORM
- Aerich (for database migrations)
- SQLite (for database)
- Pydantic
- Passlib (for password hashing)
- Python-Jose (for JWT handling)

## Getting Started

### Prerequisites

- Python 3.9+
- pip (Python package installer)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Kvazar13/task_management_api.git
    cd task_management_api
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file for environment variables:**
    ```dotenv
    # .env
    DATABASE_URL=sqlite://db.sqlite3
    SECRET_KEY=your_super_secret_key
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

### Running the Application

1. **Apply database migrations:**
    ```bash
    aerich init -t app.config.TORTOISE_ORM
    aerich init-db
    ```

2. **Start the FastAPI application:**
    ```bash
    uvicorn app.main:app --reload
    ```

    The application will be available at `http://127.0.0.1:8000`.

3. **Access the API documentation:**
    Open your browser and go to `http://127.0.0.1:8000/docs` to view and interact with the API endpoints using Swagger UI.

### Usage

1. **Register a new user:**
    - Endpoint: `POST /users/`
    - Request Body:
      ```json
      {
        "username": "your_username",
        "email": "your_email@example.com",
        "password": "your_password"
      }
      ```

2. **Log in to get an access token:**
    - Endpoint: `POST /users/token`
    - Request Body (form-data):
      - `username`: your_username
      - `password`: your_password

3. **Create a new task:**
    - Endpoint: `POST /tasks/`
    - Request Header:
      - `Authorization`: Bearer <access_token>
    - Request Body:
      ```json
      {
        "title": "Sample Task",
        "description": "This is a sample task."
      }
      ```

4. **Retrieve all tasks:**
    - Endpoint: `GET /tasks/`
    - Request Header:
      - `Authorization`: Bearer <access_token>


5. **Update a task (mark as completed):**
    - Endpoint: `PUT /tasks/{task_id}`
    - Request Header:
      - `Authorization`: Bearer <access_token>
    - Request Body:
      ```json
      {
        "completed": true
      }
      ```


### Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss any changes.

### License

This project is licensed under the MIT License.

---

Feel free to modify this README file to better fit your project's details and requirements. If you need any more sections or specific information, let me know!
