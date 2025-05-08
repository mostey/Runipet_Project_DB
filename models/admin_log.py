"""
AdminLog 테이블 모델
: 관리자 로그(이상 데이터 감지 등) 정보를 저장
"""

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from . import Base

class AdminLog(Base):
    __tablename__ = 'admin_log'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="로그 고유 ID"
    )

    action = Column(
        String(100),
        nullable=False,
        comment="실행된 관리자 action 설명"
    )

    detail = Column(
        String(500),
        nullable=True,
        comment="상세 내용"
    )

    created_at = Column(
        DateTime,
        server_default=func.current_timestamp(),
        comment="로그 생성 시각"
    )