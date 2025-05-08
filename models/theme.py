"""
Theme 테이블 모델
: 앱의 시각적 테마 정보를 저장
"""

from sqlalchemy import Column, Integer, String
from . import Base

class Theme(Base):
    __tablename__ = 'theme'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="테마 고유 ID"
    )  # 테마 식별용

    name = Column(
        String(50),
        unique=True,
        nullable=False,
        comment="테마 이름"
    )  # 예: '봄', '여름'

    description = Column(
        String(255),
        nullable=True,
        comment="테마 설명"
    )