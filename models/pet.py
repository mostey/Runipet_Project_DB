"""
Pet 테이블 모델
: 사용자가 기르는 가상 펫 정보를 저장
"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from . import Base

class Pet(Base):
    __tablename__ = 'pet'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="펫 고유 ID"
    )

    user_id = Column(
        Integer,
        ForeignKey('user.id'),
        nullable=False,
        comment="소유자 User 테이블의 id 참조"
    )  # Pet ↔ User 1:N 관계

    type = Column(
        String(50),
        nullable=False,
        comment="펫 종류"
    )  # 예: '고양이', '강아지'

    nickname = Column(
        String(50),
        nullable=False,
        comment="펫 닉네임"
    )

    experience = Column(
        Integer,
        default=0,
        comment="누적 경험치"
    )

    level = Column(
        Integer,
        default=1,
        comment="펫 레벨"
    )

    created_at = Column(
        DateTime,
        server_default=func.current_timestamp(),
        comment="펫 생성 시각"
    )