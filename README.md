# Inventory Management System API

This is an Inventory Management System API built using Django Rest Framework (DRF) and PostgreSQL, with JWT-based authentication for performing CRUD operations.

## Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

Ensure you have the following installed:
- Python
- PostgreSQL
- pip (Python package installer)

### Installation Steps

1. **Clone the repository from GitHub**  
   Download the code from GitHub and extract the zip file, or use Git:

   ```bash
   git clone <repository-url>
   cd <project-directory>


2.Install the required packages
Use pip to install all the dependencies from requirements.txt:

pip install -r requirements.txt

3.Set up the PostgreSQL database
Ensure your PostgreSQL server is running. Create a new PostgreSQL database for the project.

4.Configure the database settings
Update the settings.py file with your PostgreSQL database credentials (username, password, database name, etc.).

5.Create a superuser
To test the API, create a superuser account:

python manage.py createsuperuser

6.Apply database migrations
Run the following commands to apply migrations:

python manage.py makemigrations
python manage.py migrate

7.Run the server
Start the Django development server:

python manage.py runserver

8.Access the API
You can now access the API in your browser at:

http://127.0.0.1:8000/api

Authentication
To perform CRUD operations, you need to obtain an access token. Use the following endpoint to generate a token by providing your username and password:

POST http://127.0.0.1:8000/api/token

Example API Requests
Here are some example commands for performing CRUD operations:

1.Create an Item (Insert):

http POST http://127.0.0.1:8000/api/items/ "Authorization: Bearer <access_token>" name="Item name" description="Item details"

2.Update an Item:

http PUT http://127.0.0.1:8000/api/items/{item_id}/ "Authorization: Bearer <access_token>" name="Updated Item name" description="Updated Item details"

Delete an Item:

http DELETE http://127.0.0.1:8000/api/items/{item_id}/ "Authorization: Bearer <access_token>"

Read an Item:

http GET http://127.0.0.1:8000/api/items/{item_id}/ "Authorization: Bearer <access_token>"






