"""
PetStage 테이블 모델
: 펫 성장 단계 정보를 저장
"""

from sqlalchemy import Column, Integer, String
from . import Base

class PetStage(Base):
    __tablename__ = 'pet_stage'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="성장 단계 고유 ID"
    )

    stage_name = Column(
        String(50),
        nullable=False,
        comment="단계 이름"
    )  # 예: '알', '유년기'

    min_experience = Column(
        Integer,
        nullable=False,
        comment="이 단계로 전환 가능한 최소 경험치"
    )