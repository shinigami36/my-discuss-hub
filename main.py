from fastapi import FastAPI
from database import init_db
from routers import users, discussions, comments

app = FastAPI()

# Initialize the database
init_db()

app.include_router(users.router)
app.include_router(discussions.router)
app.include_router(comments.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to DiscussHub"}
