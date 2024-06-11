# my-discuss-hub
DiscussHub is a web application built with Python using the FastAPI framework, designed to facilitate discussions among users through posts and comments. Users can create accounts, post discussions with text and images, follow other users, and interact with posts and comments by liking, commenting, and more.

Key Features:
User Management:

User authentication (signup/login).
Profile management (update user details).
Search functionality to find other users.
Follow/unfollow functionality to connect with other users.
Discussion Features:

Create posts with text and optional images.
Add hashtags to categorize posts.
Like, comment, and reply to posts.
Edit and delete own posts and comments.
View count for each post.
Advanced Search:

Search for posts based on hashtags.
Search for posts containing specific text.
Technology Stack:
Backend:

Python
FastAPI - A modern, fast (high-performance), web framework for building APIs with Python.
SQLAlchemy - An Object-Relational Mapping (ORM) tool for Python.
Frontend:

(Specify if applicable, or mention that it's an API-only backend).
Database:

PostgreSQL - Used for storing user data, posts, comments, and other related information.
How to Run:
To run the DiscussHub project locally, follow these steps:

Clone the Repository:

bash
Copy code
git clone https://github.com/shinigami36/my-discuss-hub.git
cd my-discuss-hub
Set Up Virtual Environment:

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Set Environment Variables:
Create a .env file in the root directory of the project and configure necessary environment variables such as:

makefile
Copy code
DATABASE_URL=postgresql://your_database_url
SECRET_KEY=your_secret_key
Run Database Migrations:
If migrations are used (e.g., with Alembic), run database migrations:

bash
Copy code
alembic upgrade head
Start the FastAPI Server:

bash
Copy code
uvicorn main:app --reload
Access DiscussHub:
Open a web browser and go to http://localhost:8000 to access the DiscussHub application.

API Documentation:
Swagger UI: The FastAPI framework provides automatic interactive API documentation with Swagger UI. Once the server is running, you can access the Swagger UI documentation at http://localhost:8000/docs.
