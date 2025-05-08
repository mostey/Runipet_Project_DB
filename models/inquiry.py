"""
Inquiry 테이블 모델
: 사용자 문의 사항을 저장
"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from . import Base

class Inquiry(Base):
    __tablename__ = 'inquiry'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="문의 고유 ID"
    )

    user_id = Column(
        Integer,
        ForeignKey('user.id'),
        nullable=False,
        comment="문의자 User ID"
    )

    question = Column(
        String(500),
        nullable=False,
        comment="문의 내용"
    )

    created_at = Column(
        DateTime,
        server_default=func.current_timestamp(),
        comment="문의 작성 시각"
    )