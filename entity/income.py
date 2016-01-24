__author__ = 'rizkivmaster'


from sqlalchemy import Column, Date, String, BigInteger
from common.database.ModelBase import ModelBase
from common.database.PostgreBase import PostgresAccessorBase
from config import general_config
from enum import AccountingType

class Income(ModelBase):
    __tablename__ = 'records'
    date = Column(Date)
    accountingId = Column(String, primary_key=True)
    accountingPost = Column(String)
    accountingType = Column(String)
    notes = Column(String)
    amount = Column(BigInteger)

    def __init__(self):
        self.date = None
        self.accountingPost = None
        self.accountingId = None
        self.accountingType = None
        self.notes = None
        self.amount = None


income_accessors = PostgresAccessorBase(Income, general_config.get_database_url())
