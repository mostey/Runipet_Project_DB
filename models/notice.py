"""
Notice 테이블 모델
: 공지사항 정보를 저장
"""

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from . import Base

class Notice(Base):
    __tablename__ = 'notice'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="공지 고유 ID"
    )

    title = Column(
        String(200),
        nullable=False,
        comment="공지 제목"
    )

    content = Column(
        String(1000),
        nullable=False,
        comment="공지 내용"
    )

    posted_at = Column(
        DateTime,
        server_default=func.current_timestamp(),
        comment="게시 시각"
    )