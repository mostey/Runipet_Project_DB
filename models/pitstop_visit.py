"""
PitstopVisit 테이블 모델
: 사용자의 피트스탑 방문 기록 저장
"""

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from . import Base

class PitstopVisit(Base):
    __tablename__ = 'pitstop_visit'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="방문 기록 고유 ID"
    )

    user_id = Column(
        Integer,
        ForeignKey('user.id'),
        nullable=False,
        comment="방문자 사용자 ID"
    )

    pitstop_id = Column(
        Integer,
        ForeignKey('pitstop.id'),
        nullable=False,
        comment="방문한 피트스탑 ID"
    )

    visited_at = Column(
        DateTime,
        server_default=func.current_timestamp(),
        comment="방문 시각"
    )