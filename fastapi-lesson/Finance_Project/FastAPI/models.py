from database import Base
from sqlalchemy import column, Integer, String, Boolean, Float

class Transaction(Base):
    __tablename__ = 'transactions'

    id = column(Integer, primary_key=True, index=True)
    amount = column(Float)
    category = column(String)
    description = column(String)
    is_income = column(Boolean)
    date = column(String)

