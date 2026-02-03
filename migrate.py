from models.database import db
from models.products import Product

db.connect()
db.create_tables([ Product ])