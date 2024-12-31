from dotenv import load_dotenv
import os

load_dotenv()

# Twilio SendGrid
# SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
# SENDGRID_FROM_EMAIL = os.getenv("SENDGRID_FROM_EMAIL")

# Slack
# SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
# SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")

# MongoDB
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME","email_slack")
# MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "default_database_name")
