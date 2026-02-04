from peewee import *

from database import db

class Product(Model):
    title = CharField()
    link = CharField()
    service = CharField()
    term = CharField()
    price = DecimalField(10, 2)
    score = IntegerField()

    class Meta:
        database = db