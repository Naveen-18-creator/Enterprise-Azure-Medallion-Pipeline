import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL=os.getenv("BASE_URL")

CONNECTION_STRING=os.getenv("CONNECTION_STRING")

CONTAINER_NAME=os.getenv("CONTAINER_NAME")


