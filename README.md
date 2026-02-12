# Travel-Planner
Python engineer test assessment - Travel Planner

Tech Stack:

 - Backend: Python 3.11, Django, Django REST Framework (DRF)

 - Database: SQLite (configured for easy assessment review)

 - Caching: Redis via django-redis

 - Containerization: Docker & Docker Compose

 - API Documentation/Testing: Postman

Installation & Setup
1. Prerequisites
Ensure you have Docker and Docker Compose installed on your machine.

2. Clone & Configure
# Clone the repository
  ```sh
  git clone https://github.com/olex2211/Travel-Planner/
  ```

**Set up environment variables**

Create `.env` file in the root directory and add the following variables:

_Note: see `.env.example`_


3. Run with Docker
Build and start the containers (Django and Redis) in detached mode:

```sh
docker-compose up --build -d
```


# API Testing (Postman)

A pre-configured collection file Travel_Planner_API.postman_collection.json is included in the root directory.

 - Import the collection into Postman.

 - Happy Path: Run this folder to see the full lifecycle (Create -> Update -> Add Place -> Delete).

 - Negative Tests: Verify error handling for duplicates and the 10-place limit.

 - Pagination & Filtering: Test sorting, search queries, and page navigation.

_Note: The collection uses Postman scripts to automatically save project_id and place_id to collection variables for a seamless testing experience.(You can change URL manually if it's not working properly)_


# Teardown #
To stop and remove the containers:

```sh
docker-compose down
```
