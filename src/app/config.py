import os
from dotenv import load_dotenv

load_dotenv()

class Config:
  DBUSER = os.getenv('DBUSER')
  DBPASS = os.getenv('DBPASS')
  DBHOST = os.getenv('DBHOST')
  DBNAME = os.getenv('DBNAME')
  