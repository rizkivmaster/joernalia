from common.database import ModelBase
from common.database.PostgreBase import PostgresAccessorBase
from config import general_config
from sqlalchemy import Date, Column, String, Integer


class Item(ModelBase):
    __tablename__ = "Item"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    date_added = Column(Date)
    price = Column(Integer)
    image_url = Column(Date)

    def __init__(self):
        self.name = None
        self.date_added = None
        self.image_url = None
        self.id = None


item_accessor = PostgresAccessorBase(Item, database_url=general_config.get_database_url())
#
#
# def get_item(id):
#     return item_accessor.query(Item).filter(Item.id == id).first()
#
#
# def upset_item(item):
#     """
#     :type item:Item
#     :param item:
#     :return:
#     """
#     item_accessor.add(item) if get_item(item.id) else None
#     item_accessor.commit()
#
# def
