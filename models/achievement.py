"""
Achievement 테이블 모델
: 사용자 업적 정보를 저장
"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from . import Base

class Achievement(Base):
    __tablename__ = 'achievement'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="업적 고유 ID"
    )

    user_id = Column(
        Integer,
        ForeignKey('user.id'),
        nullable=False,
        comment="User 테이블의 id 참조"
    )

    name = Column(
        String(100),
        nullable=False,
        comment="업적 이름"
    )

    achieved_at = Column(
        DateTime,
        server_default=func.current_timestamp(),
        comment="달성 시각"
    )