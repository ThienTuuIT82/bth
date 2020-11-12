from saleapp import db
from sqlalchemy import Column, Integer, Boolean, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class SaleBase(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(50), nullable=False)


class Category(SaleBase):
    __tablename__ = 'category'

    product = relationship('Product', backref='category', lazy=True)


class Product(SaleBase):
    __tablename__ = 'product'
    decription = Column(String(255))
    price = Column(Integer,default=0)
    image = Column(String(100))
    catgory_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    db.create_all()