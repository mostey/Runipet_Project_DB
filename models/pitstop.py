"""
Pitstop 테이블 모델
: 피트스탑 위치 정보를 저장
"""

from sqlalchemy import Column, Integer, String, Float
from . import Base

class Pitstop(Base):
    __tablename__ = 'pitstop'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="피트스탑 고유 ID"
    )

    name = Column(
        String(100),
        nullable=False,
        comment="피트스탑 이름"
    )

    latitude = Column(
        Float,
        nullable=False,
        comment="위도"
    )

    longitude = Column(
        Float,
        nullable=False,
        comment="경도"
    )