"""
SocialRelation 테이블 모델
: 사용자 간 친구 관계 정보를 저장
"""

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from . import Base

class SocialRelation(Base):
    __tablename__ = 'social_relation'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="관계 고유 ID"
    )

    user_id = Column(
        Integer,
        ForeignKey('user.id'),
        nullable=False,
        comment="요청자 사용자 ID"
    )

    friend_id = Column(
        Integer,
        ForeignKey('user.id'),
        nullable=False,
        comment="수신자 사용자 ID"
    )

    created_at = Column(
        DateTime,
        server_default=func.current_timestamp(),
        comment="친구 요청 시각"
    )