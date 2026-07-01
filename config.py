import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL=os.getenv("BASE_URL")

CONNECTION_STRING=os.getenv("CONNECTION_STRING")

BRONZE_CONTAINER=os.getenv("BRONZE_CONTAINER")
SILVER_CONTAINER=os.getenv("SILVER_CONTAINER")
GOLD_CONTAINER=os.getenv("GOLD_CONTAINER")