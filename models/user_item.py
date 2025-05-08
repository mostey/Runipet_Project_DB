"""
UserItem 테이블 모델
: 사용자와 아이템 간 소유 관계 저장
"""

from sqlalchemy import Column, Integer, ForeignKey
from . import Base

class UserItem(Base):
    __tablename__ = 'user_item'

    user_id = Column(
        Integer,
        ForeignKey('user.id'),
        primary_key=True,
        comment="User 테이블의 id 참조"
    )

    item_id = Column(
        Integer,
        ForeignKey('item.id'),
        primary_key=True,
        comment="Item 테이블의 id 참조"
    )

    quantity = Column(
        Integer,
        default=1,
        comment="소유 수량"
    )  # 사용자가 보유한 아이템 개수