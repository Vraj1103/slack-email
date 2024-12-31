# app/main.py
from fastapi import FastAPI
from app.routes import email, slack
from app.utils.database import is_db_connected

app = FastAPI(title="Email-Slack Integration")

# Register routes
app.include_router(email.router, prefix="/email", tags=["Email"])
app.include_router(slack.router, prefix="/slack", tags=["Slack"])

@app.get("/")
async def check_db_connection():
    if is_db_connected():
        return {"status": "Database is connected successfully!"}
    return {"status": "Failed to connect to the database."}

