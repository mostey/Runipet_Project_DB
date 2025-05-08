"""
Item 테이블 모델
: 아이템 정보를 저장
"""

from sqlalchemy import Column, Integer, String, Float
from . import Base

class Item(Base):
    __tablename__ = 'item'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="아이템 고유 ID"
    )

    name = Column(
        String(100),
        nullable=False,
        comment="아이템 이름"
    )

    price = Column(
        Integer,
        nullable=False,
        comment="아이템 가격(코인)"
    )