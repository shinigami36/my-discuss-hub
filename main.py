from fastapi import FastAPI
from routers import users, discussions, comments
from database import engine, Base

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(discussions.router)
app.include_router(comments.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to DiscussHub"}
