from peewee import *

from models.database import db

class Product(Model):
    title = CharField()
    link = CharField()
    service = CharField()
    price = CharField()

    class Meta:
        database = db