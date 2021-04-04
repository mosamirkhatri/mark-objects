import os

class Config:
    class MySql:
        DATABASE_SERVER = os.getenv('RDS_SERVER')
        DATABASE_NAME = os.getenv('RDS_DB')
        DATABASE_USER = os.getenv('RDS_USER')
        DATABASE_PASS = os.getenv('RDS_PASS')
