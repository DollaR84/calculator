"""
Config module for the calculator.

created on 10.06.2020

@author: Ruslan Dolovanyuk

"""

import os


class Database:

    def __init__(self):
        self.host: str = os.getenv('HOST')
        self.port: int = os.getenv('PORT')
        self.db_name: str = os.getenv('DB_NAME')


class Settings:

    def __init__(self):
        self.db = Database()
