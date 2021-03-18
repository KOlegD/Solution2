import sqlalchemy
from .db_session import SqlAlchemyBase


class Table1(SqlAlchemyBase):
    __tablename__ = 'table1'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
