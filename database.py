"""
Database module for the calculator.

created on 10.06.2020

@author: Ruslan Dolovanyuk

"""

from pymongo import MongoClient

from models import OperationModel


class Database:

    def __init__(self, settings):
        self.settings = settings

    async def open(self):
        self.client = MongoClient(self.settings.host, self.settings.port)
        self.db = self.client[self.settings.db_name]
        self.history = self.db.history

    async def close(self):
        self.client.close()

    async def add(self, operation: OperationModel):
        await self.open()
        self.history.insert_one(operation)
        await self.close()
